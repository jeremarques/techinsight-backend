from rest_framework import serializers


class CustomDateField(serializers.DateField):
    def to_internal_value(self, value):
        if value == "":
            return None
        return super(CustomDateField, self).to_internal_value(value)
    

class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    profile_photo = serializers.URLField()
    website_url = serializers.URLField()
    bio = serializers.CharField()
    about = serializers.CharField()
    date_of_birth = serializers.DateField(format="%Y-%m-%d")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")


class UserProfileCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    profile_photo = serializers.URLField()
    website_url = serializers.URLField()
    bio = serializers.CharField(max_length=200)
    about = serializers.CharField()
    date_of_birth = CustomDateField(allow_null=True, format="%Y-%m-%d")

