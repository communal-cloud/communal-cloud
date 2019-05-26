from rest_framework.serializers import ModelSerializer
from cc import models


class ExecutionSerializer(ModelSerializer):
    class Meta:
        model = models.Execution
        fields = ("id", "Task", "Data", "ExecutedBy")
