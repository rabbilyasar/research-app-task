from rest_framework import generics
from .serializers import TaskSerializer, TileSerializer
from .models import Task, Tile


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TileSerializer
    queryset = Tile.objects.all()


class TileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TileSerializer
    queryset = Tile.objects.all()