from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from school.models import Course, Lesson, Payment, Following
from school.permissions import IsStaff, IsOwner, ViewSetPermission, NotIsStaff
from school.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, FollowingSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (ViewSetPermission, )


class LessonAPIList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsAdminUser]


class LessonAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsStaff | IsOwner | IsAdminUser]


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
    permission_classes = [IsStaff | IsOwner | IsAdminUser]


class LessonAPIDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]


class PaymentAPIList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
    permission_classes = [IsOwner | IsAdminUser]


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
    permission_classes = [IsOwner | IsAdminUser]
