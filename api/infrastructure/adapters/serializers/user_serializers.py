from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from api.validators import validate_username


class UserReadSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    followers = serializers.IntegerField()
    following = serializers.IntegerField()
    is_follower = serializers.BooleanField()
    is_active = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)


class UserPostReadSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    username = serializers.CharField()
    is_follower = serializers.BooleanField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)


class UserCreateSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    full_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if not validate_username(attrs.get('username')):
            raise serializers.ValidationError({"username": "O nome de usuário deve conter apenas letras, números, '_' e '.'"})

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"password": "As senhas devem ser iguais."})

        return attrs


class UserEditSerializer(serializers.Serializer):

    new_username = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)

