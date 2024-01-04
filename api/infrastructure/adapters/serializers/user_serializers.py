from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from api.validators import validate_username

from api.models.user import User

class UserReadSerializer(serializers.ModelSerializer):

    is_active = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'full_name',
            'is_active',
            'created_at',
        )


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

