from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.post_comment import CreatePostCommentUseCase
from api.infrastructure.adapters.repositories.post_comment import PostCommentRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.serializers.post_comment_serializers import PostCommentSerializer
from api.errors import NotFoundException


class ListCreatePostCommentView(APIView):

    def post(self, request: Dict[str, Any], *args, **kwargs):

        profile_id = request.user.profile.id
        post_id = kwargs.get('post_id')

        post_content = request.data.get('content')
        
        use_case = CreatePostCommentUseCase(PostCommentRepository(), PostRepository(), UserProfileRepository())
        try:
            post_comment = use_case.execute(profile_id, post_id, post_content)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_comment_serialized = PostCommentSerializer(post_comment)
        body = post_comment_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
    

