from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from school.models import Lesson


class LessonApiTestCAse(APITestCase):
    url = '/lesson/'
    patched_url = '/lesson/1/'
    not_found = {'detail': 'Not found.'}
    patch_url = '/lesson/edit/1/'
    delete_url = 'lesson/delete/1'
    data = {
            "id": 1,
            "title": "test",
            "description": "test",
            "lint": "https://www.youtube.com/"
        }
    patch_data = {
            "id": 1,
            "title": "test1",
            "description": "test1",
            "lint": "https://www.youtube.com/"
        }
    def setUp(self) -> None:
        Lesson.objects.create(
            id=1,
            title='test',
            description='test',
            link='https://www.youtube.com/'
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patch(self):
        self.client.patch(self.patch_url, self.patch_data)
        response = self.client.get(self.patched_url)
        self.assertEqual(response.json(), self.patch_data)

    def test_delete(self):
        self.client.delete(self.delete_url)
        response = self.client.get(self.patched_url)
        self.assertEqual(response.json(), self.not_found)




