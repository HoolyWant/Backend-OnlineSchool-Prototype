import os

import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from school.models import Course, Lesson, Payment, Following
from school.permissions import IsOwnerOrStuff, ViewSetPermission, NotIsStaff, IsOwner
from school.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, FollowingSerializer
from school.services import create_product, create_price, create_session
from school.tasks import send_update
from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (ViewSetPermission, )

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()

    def perform_update(self, serializer):
        update_course = serializer.save()
        followers = Following.objects.filter(course_id=update_course.id)
        followers_list = []
        course_title = update_course.title
        for follower in followers:
            followers_list.append(User.objects.get(pk=follower.user_id).__dict__['email'])
        send_update(followers_list, course_title)
        update_course.save()


class LessonAPIList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | NotIsStaff]


class LessonAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStuff]


class LessonAPICreate(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [NotIsStaff | IsAdminUser | IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonAPIEdit(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStuff]

    def perform_update(self, serializer):
        update_lesson = serializer.save()
        if update_lesson.course_id:
            followers = Following.objects.filter(course_id=update_lesson.course_id)
            followers_list = []
            lesson_title = update_lesson.title
            for follower in followers:
                followers_list.append(User.objects.get(
                    pk=follower.user_id).__dict__['email'])
            send_update.delay(followers_list, lesson_title)
        update_lesson.save()


class LessonAPIDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsAdminUser]


class PaymentCreateAPI(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [NotIsStaff | IsAdminUser]

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user_id = self.request.user
        if new_payment.course is not None and new_payment.lesson is None:
            new_payment.amount = Course.objects.get(pk=new_payment.course.__dict__['id']).cost
            if new_payment.payment_method == 'card':
                stripe.api_key = os.getenv('STRIPE_API_KEY')
                product_name = Course.objects.get(pk=new_payment.course.__dict__['id']).title
                new_product = create_product(product_name)
                new_price = create_price(new_product, new_payment.amount)
                new_session = create_session(new_price)
                new_payment.link = new_session['url']
                new_payment.save()
        elif new_payment.lesson is not None and new_payment.course is None:
            new_payment.amount = Lesson.objects.get(pk=new_payment.lesson.__dict__['id']).cost
            if new_payment.payment_method == 'card':
                stripe.api_key = os.getenv('STRIPE_API_KEY')
                product_name = Lesson.objects.get(pk=new_payment.lesson.__dict__['id']).title
                new_product = create_product(product_name)
                new_price = create_price(new_product, new_payment.amount)
                new_session = create_session(new_price)
                new_payment.link = new_session['url']
                new_payment.save()
        elif new_payment.lesson is not None and new_payment.course is not None:
            raise 'Нужно выбрать либо урок, либо курс для оплаты'
        else:
            raise 'Ни один из курсов или уроков не выбраны'


class PaymentAPIList(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
    permission_classes = [IsAdminUser]


class PaymentAPIVIew(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsOwnerOrStuff]


class FollowingCreateApi(generics.CreateAPIView):
    serializer_class = FollowingSerializer
    permission_classes = [NotIsStaff | IsAdminUser | IsAuthenticated]

    def perform_create(self, serializer):
        new_following = serializer.save()
        if new_following.following_status:
            new_following.user = self.request.user
        new_following.save()


class FollowingDestroyApi(generics.DestroyAPIView):
    serializer_class = FollowingSerializer
    queryset = Following.objects.all()
    permission_classes = [IsOwnerOrStuff]
