from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.relationship import FollowUserUseCase, UnfollowUserUseCase
from api.infrastructure.adapters.repositories.relationship import RelationshipRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.serializers.relationship_serializers import RelationshipSerializer
from api.errors import NotFoundException, AlreadyExistsException


class CreateFollowView(APIView):

    def post(self, request: Dict[str, Any], *args, **kwargs):
        follower_id = request.user.id
        followed_id = int(kwargs.get("user_id"))

        use_case = FollowUserUseCase(RelationshipRepository(), UserRepository())
        
        try:
            follow_entity = use_case.execute(follower_id, followed_id)
        
        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except AlreadyExistsException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_400_BAD_REQUEST)

        follow_serialized = RelationshipSerializer(follow_entity)
        body = follow_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)


class DeleteFollowView(APIView):

    def delete(self, request: Dict[str, Any], *args, **kwargs):
        follower_id = request.user.id
        followed_id = int(kwargs.get("user_id"))

        use_case = UnfollowUserUseCase(RelationshipRepository())

        try:
            use_case.execute(follower_id, followed_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)