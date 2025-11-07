from rest_framework import serializers
from .models import Task

class TaskModelSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = '__all__'
