import json
from pprint import pprint

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson, Course
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

        self.model = Lesson.objects.create(title='test3', description='test3', link="https://www.youtube.com/")

    def test_get(self):
        response = self.client.get(reverse('school:lesson_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post(reverse('school:lesson_create'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        response = self.client.patch(f'/lesson/edit/{self.model.id}', data=self.patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(f'/lesson/delete/{self.model.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FollowingApiTestCAse(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin_test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.model = Course.objects.create(title='title', description='description')
        self.data = {
            "course": self.model.id
        }

    def test_post(self):
        response = self.client.post(reverse('school:following_create'), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PaymentApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin_test', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)
        self.model = Course.objects.create(title='test3', description='test3', cost=1000)
        self.pay = {
            'course': self.model.id,
            'payment_method': 'card'
        }

    def test_get(self):
        response = self.client.get('/payment/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post(reverse('school:payment_create'), data=self.pay)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)























