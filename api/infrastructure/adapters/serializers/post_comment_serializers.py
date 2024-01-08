from rest_framework import serializers
from .user_profile_serializers import UserProfilePostSerializer

class PostCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile = UserProfilePostSerializer()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")