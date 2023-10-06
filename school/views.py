from django.shortcuts import render
from rest_framework import viewsets, generics

from school.models import Course, Lesson
from school.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonAPIList(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonAPICreate(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonAPIEdit(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonAPIDelete(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

