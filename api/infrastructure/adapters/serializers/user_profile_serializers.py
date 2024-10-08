from rest_framework import serializers
from .user_serializers import UserPostReadSerializer, UserPostResumeReadSerializer, UserReadSerializer


class CustomDateField(serializers.DateField):
    def to_internal_value(self, value):
        if value == "":
            return None
        return super(CustomDateField, self).to_internal_value(value)
    

class UserProfileReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserReadSerializer(read_only=True)
    name = serializers.CharField(max_length=60)
    profile_photo = serializers.URLField()
    posts = serializers.IntegerField()
    website_url = serializers.URLField()
    bio = serializers.CharField(max_length=200)
    about = serializers.CharField()
    date_of_birth = CustomDateField(allow_null=True, format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class UserProfilePostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserPostReadSerializer(read_only=True)
    name = serializers.CharField(max_length=60)
    profile_photo = serializers.URLField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class UserProfilePostResumeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserPostResumeReadSerializer(read_only=True)
    profile_photo = serializers.URLField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class UserProfileCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60, required=False)
    profile_photo = serializers.URLField(allow_blank=True, required=False)
    website_url = serializers.URLField(allow_blank=True, required=False)
    bio = serializers.CharField(max_length=200, allow_blank=True, required=False)
    about = serializers.CharField(allow_blank=True, required=False)
    date_of_birth = CustomDateField(allow_null=True, format="%Y-%m-%d", required=False)

