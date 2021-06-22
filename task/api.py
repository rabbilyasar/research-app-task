from task.models import Task
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, TileListCreateAPIView, TileRetrieveUpdateDestroyAPIView

app_name = 'task'

urlpatterns = [
    path('task', TaskListCreateAPIView.as_view(), name='task-create-list'),
    path('task/<str:pk>', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-update-delete'),
    path('tile', TileListCreateAPIView.as_view(), name='tile-create-list'),
    path('tile/<str:pk>', TileRetrieveUpdateDestroyAPIView.as_view(), name='tile-update-delete'),
]