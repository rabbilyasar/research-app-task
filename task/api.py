from task.models import Task
from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task-create-list'),
    path('<str:pk>', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-update-delete'),
]