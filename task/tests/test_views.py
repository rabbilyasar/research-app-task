from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from task.models import Task, Tile


class TestViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test_user', email='test@user.com', password='test123')
        cls.tile = Tile.objects.create(launch_date=timezone.now(), status='live')
        cls.task1 = Task.objects.create(user=cls.user,
                                        tile=cls.tile,
                                        title='test title',
                                        description='test description',
                                        type='survey')
        cls.task2 = Task.objects.create(user=cls.user,
                                        tile=cls.tile,
                                        title='test title1',
                                        description='test description1',
                                        type='survey')

    def test_unauthorized_user_for_403(self):
        response = self.client.get(reverse('task:task-create-list'))
        self.assertTrue(status.is_client_error(response.status_code))


    def test_task_can_be_created(self):
        self.client.login(username=self.user.username, password='test123')
        data = {
            "user": self.user.id,
            "tile": self.tile,
            "title": "test title",
            "description": "Test description",
            "type": "survey"
        }
        response = self.client.post(reverse('task:task-create-list'), data=data)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['user'], self.user.id)
        self.assertEqual(response.data['tile'], self.tile.id)
        self.assertEqual(Task.objects.count(), 3)

    def test_task_can_be_updated(self):
        self.client.login(username=self.user.username, password='test123')
        response = self.client.patch(reverse('task:task-update-delete',
                                            args=[self.task1.id]),
                                            data={'order_field': 1})
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['order_field'], 1)

    def test_tile_can_have_multiple_task(self):
        tile = Tile.objects.get(id=1)
        count = tile.tasks.count()
        self.assertEqual(count, 2)

    def test_tile_can_be_created(self):
        self.client.login(username=self.user.username, password='test123')
        data = {
            "launch_date": timezone.now(),
            "status": "live"
        }
        response = self.client.post(reverse('task:tile-create-list'), data=data)
        self.assertTrue(status.is_success(response.status_code))


