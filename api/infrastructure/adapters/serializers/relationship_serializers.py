from rest_framework import serializers

class RelationshipSerializer(serializers.Serializer):
    follower_id = serializers.IntegerField()
    followed_id = serializers.IntegerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    