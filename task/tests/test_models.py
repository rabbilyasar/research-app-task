from django.test import TestCase
from task.models import Task, Tile
from django.contrib.auth.models import User
from django.utils import timezone


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        """setup data for test
        """
        cls.user = User.objects.create(username='testuser',
                                       email='test@mail.com',
                                       password='test123')
        cls.tile = Tile.objects.create(launch_date=timezone.now(),
                                       status='live')
        cls.task1 = Task.objects.create(user=cls.user,
                                        title='test title',
                                        description='test description',
                                        type='survey',
                                        tile=cls.tile)
        cls.task2 = Task.objects.create(user=cls.user,
                                        title='test title1',
                                        description='test description1',
                                        type='survey',
                                        tile=cls.tile)

    def test_task_is_created(self):
        self.assertIsInstance(self.task1, Task)

    def test_task_belongs_to_the_tile(self):
        self.assertEqual(self.task1.tile, self.tile)

    def test_task_have_user(self):
        self.assertEqual(self.task1.user, self.user)

    def test_tile_is_created(self):
        self.assertIsInstance(self.tile, Tile)

    def test_tile_count_in_tile(self):
        task_count = self.tile.tasks.all().count()
        self.assertEqual(task_count, 2)
