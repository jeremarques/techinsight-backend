from rest_framework import serializers

class ProfileReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    profile_photo = serializers.URLField()
    website_url = serializers.URLField()
    bio = serializers.CharField()
    about = serializers.CharField()
    date_of_birth = created_at = serializers.DateField(format="%Y-%m-%d")
    created_at = created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")