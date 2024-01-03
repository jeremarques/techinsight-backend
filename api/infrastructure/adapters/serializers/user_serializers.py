from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

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
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    full_name = serializers.CharField(required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({"password": "As senhas devem ser iguais."})

        return attrs


class UserEditSerializer(serializers.Serializer):

    new_username = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)

    def validate(self, attrs):
        new_username = attrs.get('new_username')
        current_username = attrs.get('username')
        email = attrs.get('email')

        if new_username and User.objects.filter(username=new_username).exclude(username=current_username).exists():
            raise serializers.ValidationError({"new_username": "Este username já está em uso."})

        if email and User.objects.filter(email=email).exclude(username=current_username).exists():
            raise serializers.ValidationError({"email": "Este email já está em uso."})

        return attrs