
from rest_framework import serializers
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'password', 'is_active', 'is_superuser')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 255,
            }
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RenovationSerializer(serializers.Serializer):
    tk_renovation = serializers.CharField()

class LogoutSerializer(serializers.Serializer):
    tk_renovation = serializers.CharField()