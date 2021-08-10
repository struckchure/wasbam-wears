from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'date',
            'updated'
        ]
        read_only_fields = [
            'is_staff',
            'is_superuser',
            'is_active',
        ]


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
