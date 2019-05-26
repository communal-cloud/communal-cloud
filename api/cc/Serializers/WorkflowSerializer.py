from rest_framework.serializers import ModelSerializer
from cc import models


class WorkflowSerializer(ModelSerializer):
    class Meta:
        model = models.Workflow
        fields = '__all__'