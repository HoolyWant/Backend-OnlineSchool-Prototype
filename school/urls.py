from django.urls import path

from school.apps import SchoolConfig
from school.views import CourseViewSet, LessonAPIList, LessonAPICreate, LessonAPIView, LessonAPIEdit, LessonAPIDelete, \
    FollowingCreateApi, FollowingDestroyApi, PaymentCreateAPI, PaymentAPIList, PaymentAPIVIew
from rest_framework.routers import DefaultRouter

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/', LessonAPIList.as_view(), name='lesson_list'),
    path('lesson/create/', LessonAPICreate.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', LessonAPIView.as_view(), name='lesson_view'),
    path('lesson/edit/<int:pk>', LessonAPIEdit.as_view(), name='lesson_edit'),
    path('lesson/delete/<int:pk>', LessonAPIDelete.as_view(), name='lesson_delete'),
    path('following/create/', FollowingCreateApi.as_view(), name='following_create'),
    path('following/delete/<int:pk>', FollowingDestroyApi.as_view(), name='following_delete'),
    path('payment/create/', PaymentCreateAPI.as_view(), name='payment_create'),
    path('payment/', PaymentAPIList.as_view(), name='payment_list'),
    path('payment/<int:pk>', PaymentAPIVIew.as_view(), name='payment_view'),
] + router.urls
