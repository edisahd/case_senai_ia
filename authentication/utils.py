from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from typing import Dict
from authentication.serializers import UserModelSerializer

def create_authentication_payload(refresh_token: RefreshToken, user: User) -> Dict:
    return {
        'tk_renovation': str(refresh_token),
        'tk_access': str(refresh_token.access_token),
        'user': UserModelSerializer(user).data,
    }
