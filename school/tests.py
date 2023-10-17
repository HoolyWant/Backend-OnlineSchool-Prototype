import json

from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APITestCase

from school.models import Lesson
from users.models import User


class LessonApiTestCAse(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin_test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.data = {
            "title": "test",
            "description": "test",
            "link": "https://www.youtube.com/"
        }
        self.patch_data = {
            "title": "test1",
            "description": "test1",
            "link": "https://www.youtube.com/"
        }

    def test_get(self):
        response = self.client.get(reverse('school:lesson_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post(reverse('school:lesson_create'), data=self.data)
        # request = self.client.get('/lesson/1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(request, self.data)

    def test_patch(self):
        response = self.client.patch('/lesson/edit/1', self.patch_data)
        request = self.client.get('/lesson/1')
        # self.assertEqual(request.json(), self.patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete('/lesson_delete/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



