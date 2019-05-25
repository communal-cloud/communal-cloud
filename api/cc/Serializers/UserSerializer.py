from rest_framework.serializers import ModelSerializer
from cc import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password', 'is_active', 'last_login', 'groups', 'user_permissions', 'is_superuser', 'is_staff']