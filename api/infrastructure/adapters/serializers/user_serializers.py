from rest_framework import serializers
from api.models import User

class PublicUserReadSerializer(serializers.ModelSerializer):

    is_active = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'full_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'created_at',
        )