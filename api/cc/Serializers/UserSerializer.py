from rest_framework.serializers import ModelSerializer
from cc import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password', 'id', 'is_active', 'last_login']