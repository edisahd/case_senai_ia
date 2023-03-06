from django.db import DatabaseError
from rest_framework.views import APIView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from authentication.serializers import LoginSerializer, LogoutSerializer, RenovationSerializer
from authentication.utils import create_authentication_payload
from core.utils import logger, response, error_response
from rest_framework import status
from authentication.messages import Message
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import traceback
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

class LoginView(APIView):
    permission_classes = (AllowAny, )
    message = Message()

    def post(self, request: HttpRequest) -> HttpResponse:
        logger(
            location = 'authentication/view/LoginView/post',
            log = 'Request to api/authentication/login/'
        )
        serialized = LoginSerializer(data=request.data)
        if serialized.is_valid():
            try:
                user = authenticate(
                    username = serialized.data['username'],
                    password = serialized.data['password'],
                )
                if user:
                    tk_refresh = RefreshToken.for_user(user)
                    payload = create_authentication_payload(
                        refresh_token=tk_refresh, 
                        user=user
                    )
                    logger(
                        location = 'authentication/view/LoginView/post',
                        log = user.get_username() + " has logged in"
                    )
                    return response(
                        data=payload, 
                        status_response=status.HTTP_200_OK
                    )
                logger(
                    location = 'authentication/view/LoginView/post',
                    log = '[401] - ' + self.message.invalid_credentials
                )
                return error_response(
                    msg=self.message.invalid_credentials, 
                    status_response=status.HTTP_401_UNAUTHORIZED
                )
            except DatabaseError:
                logger(
                    location = 'authentication/view/LoginView/post',
                    log = '[500] - (DatabaseError) ' + self.message.server_error + ": \n" + traceback.format_exc()
                )
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            except Exception:
                logger(
                    location = 'authentication/view/LoginView/post',
                    log = '[500] - (Exception) ' + self.message.server_error + ": \n" + traceback.format_exc()
                )
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        logger(
            location = 'authentication/view/LoginView/post',
            log = '[400] - ' + self.message.invalid_input
        )
        return error_response(
            msg=self.message.invalid_input, 
            status_response=status.HTTP_400_BAD_REQUEST
        )

class RenovateView(APIView):
    permission_classes = (AllowAny, )
    message = Message()

    def post(self, request: HttpRequest) -> HttpResponse:
        logger(
            location = 'authentication/view/RenovateView/post',
            log = 'Request to api/authentication/login/'
        )
        serialized = RenovationSerializer(data=request.data)
        if serialized.is_valid():
            try:
                tk_refresh = RefreshToken(serialized.data['tk_renovation'])
                outstanding_token = OutstandingToken.objects.get(token = serialized.data['tk_renovation'])
                user = User.objects.get(id = outstanding_token.user_id)
                payload = create_authentication_payload(
                    refresh_token = tk_refresh,
                    user = user
                )
                logger(
                    location = 'authentication/view/RenovateView/post',
                    log = user.get_username() + " has renovated token"
                )
                return response(
                    data=payload, 
                    status_response=status.HTTP_200_OK
                )
            except TokenError:
                logger(
                    location = 'authentication/view/RenovateView/post',
                    log = '[406] - (TokenError) ' + self.message.bad_renovation_token + ": \n" + traceback.format_exc()
                )
                return error_response(
                    msg=self.message.bad_renovation_token, 
                    status_response=status.HTTP_406_NOT_ACCEPTABLE
                )
            except DatabaseError:
                logger(
                    location = 'authentication/view/RenovateView/post',
                    log = '[500] - (DatabaseError) ' + self.message.server_error + ": \n" + traceback.format_exc()
                )
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            except Exception:
                logger(
                    location = 'authentication/view/RenovateView/post',
                    log = '[500] - (Exception) ' + self.message.server_error + ": \n" + traceback.format_exc()
                )
                return error_response(
                    msg=self.message.server_error, 
                    status_response=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        logger(
            location = 'authentication/view/RenovateView/post',
            log = '[400] - ' + self.message.invalid_input
        )
        return error_response(
            msg=self.message.invalid_input, 
            status_response=status.HTTP_400_BAD_REQUEST
        )

class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )
    message = Message()

    def post(self, request: HttpRequest) -> HttpResponse:
        
        serialized = LogoutSerializer(data = request.data)
        if serialized.is_valid():
            outstanding_token = OutstandingToken.objects.filter(
                user_id=request.user.id, 
                token = serialized.data['tk_renovation']
            )
            for token in outstanding_token:
                blacklist = BlacklistedToken.objects.filter(token_id = token.id).first()
                if blacklist == None:
                    tk_refresh = RefreshToken(token.token)
                    tk_refresh.blacklist()
        return response(data=None, status_response=status.HTTP_200_OK)




    '''
    outstanding_token = OutstandingToken.objects.filter(user_id=request.user.id)
    for t in outstanding_token:
        blacklist = BlacklistedToken.objects.filter(token_id=t.id).first()
        if blacklist == None:
            tk_refresh = RefreshToken(
                t.token,
            )
            tk_refresh.blacklist()
    return response(data={'msg': self.message.user_logged_out}, status_response=status.HTTP_200_OK)
    '''