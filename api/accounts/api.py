from rest_framework.generics import GenericAPIView as View
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from accounts.models import User
from accounts.serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer
)


class UserDetailAPI(View):

    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        user_serializer = self.get_serializer(user)

        token, _ = Token.objects.get_or_create(
            user=user
        )

        response = Response(
            {
                'user': user_serializer.data,
                'token': token.key
            }
        )
        return response


class RegisterAPI(View):

    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data
        register_serializer = self.get_serializer(data=user_data)
        register_serializer.is_valid(raise_exception=True)
        register_serializer.save()

        username = register_serializer.validated_data.get('username')
        password = register_serializer.validated_data.get('password')

        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()

        token, _ = Token.objects.get_or_create(
            user=user
        )

        response = Response(
            {
                'user': UserSerializer(
                    user
                ).data,
                'token': token.key
            }
        )

        return response


class LoginAPI(View):

    serializer_class = LoginSerializer

    def post(self, request):
        user_cred = request.data
        login_serializer = self.get_serializer(data=user_cred)
        login_serializer.is_valid(raise_exception=True)

        username = login_serializer.validated_data.get('username')
        password = login_serializer.validated_data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            return Response(
                {
                    'error': ['Invalid credentials']
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)

        token, _ = Token.objects.get_or_create(
            user=user
        )
        user_data = UserSerializer(user).data

        response = Response(
            {
                'user': user_data,
                'token': token.key
            }
        )

        return response


class LogoutAPI(View):

    def get(self, request):
        logout(request)

        return redirect('accounts:login')
