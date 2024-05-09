from rest_framework import serializers
from .post_tag_serializers import PostTagSerializer
from .user_profile_serializers import UserProfilePostResumeSerializer, UserProfilePostSerializer
    

class PostReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    public_id = serializers.CharField()
    profile = UserProfilePostSerializer(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField()
    content = serializers.CharField()
    tag = PostTagSerializer(read_only=True)
    likes = serializers.IntegerField()
    comments = serializers.IntegerField()
    is_liked = serializers.BooleanField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class PostResumeReadSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    public_id = serializers.CharField()
    profile = UserProfilePostResumeSerializer(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField()
    tag = PostTagSerializer(read_only=True)
    likes = serializers.IntegerField()
    comments = serializers.IntegerField()
    is_liked = serializers.BooleanField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    

class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    slug = serializers.SlugField(max_length=120)
    content = serializers.CharField()
    tag_id = serializers.IntegerField(allow_null=True, required=False)


class PostUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    content = serializers.CharField()
