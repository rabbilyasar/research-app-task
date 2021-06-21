from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Model representing the task
    """
    TYPES_CHOICES = [
        ('survey', 'Survey'),
        ('discussion', 'Discussion'),
        ('diary', 'Diary'),
    ]
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=55)
    order_field = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(max_length=155)
    type = models.CharField(max_length=10, choices=TYPES_CHOICES)
    tile = models.ForeignKey('Tile', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.user}, {self.title}, {self.tile.id}'


class Tile(models.Model):
    """Model to represent the tile
    """
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('pending', 'Pending'),
        ('archived', 'Archived'),
    )
    launch_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.id}'

