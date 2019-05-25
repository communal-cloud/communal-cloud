from rest_framework.serializers import ModelSerializer
from cc import models

class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields='__all__'