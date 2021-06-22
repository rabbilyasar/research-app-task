from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
