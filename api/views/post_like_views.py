from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.domain.use_cases.post_like import CreatePostLikeUseCase, DeletePostLikeUseCase
from api.infrastructure.adapters.repositories.post_like import PostLikeRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.serializers.post_like_serializer import PostLikeSerializer
from api.errors import NotFoundException, AlreadyExistsException


class CreateAndDeletePostLikeView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request: Dict[str, Any], *args, **kwargs):

        profile_id = request.user.profile.id
        post_id = kwargs.get('post_id')
        
        use_case = CreatePostLikeUseCase(PostLikeRepository(), PostRepository())
        try:
            post_like = use_case.execute(profile_id, post_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except AlreadyExistsException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_like_serialized = PostLikeSerializer(post_like)
        body = post_like_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
    
    def delete(self, request: Dict[str, Any], *args, **kwargs):
        
        profile_id = request.user.profile.id
        post_id = kwargs.get('post_id')

        use_case = DeletePostLikeUseCase(PostLikeRepository())

        try:
            use_case.execute(profile_id, post_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

