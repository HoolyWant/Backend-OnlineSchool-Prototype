from rest_framework import serializers

from school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lesson_count', 'lesson']


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer

    class Meta:
        model = Lesson
        fields = ['title', 'description', 'image', 'link', 'course']
