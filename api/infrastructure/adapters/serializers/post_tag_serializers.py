from rest_framework import serializers

class PostTagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    slug = serializers.SlugField(max_length=70)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)