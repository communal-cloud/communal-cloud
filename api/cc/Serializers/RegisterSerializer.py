from rest_framework.serializers import ModelSerializer
from cc import models

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

        def create(self, validated_data):
            user = models.User(
                username = validated_data['username'],
                name = validated_data['name'],
                email = validated_data['email'],
                password = validated_data['password'],
            )

            return user