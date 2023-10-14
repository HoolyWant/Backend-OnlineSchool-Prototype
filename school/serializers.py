from rest_framework import serializers

from school.models import Course, Lesson, Payment
from school.permissions import IsOwner


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'image', 'link']


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lesson_count', 'lesson']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['user', 'payment_date', 'course', 'lesson', 'amount', 'payment_method']
        permission_classes = [IsOwner]

