from rest_framework import serializers

class PostLikeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    profile_id = serializers.IntegerField()
    post_id = serializers.UUIDField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")