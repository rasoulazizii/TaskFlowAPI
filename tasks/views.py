from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskModelSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskModelSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    

    