from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from api.domain.use_cases.post_comment import CreatePostCommentUseCase, ListPostCommentsUseCase, UpdatePostCommentUseCase, DeletePostCommentUseCase
from api.infrastructure.adapters.repositories.post_comment import PostCommentRepository
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.serializers.post_comment_serializers import PostCommentSerializer
from api.errors import NotFoundException, ForbiddenException


class ListCreatePostCommentView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Dict[str, Any], *args, **kwargs):

        profile_id = request.user.profile.id
        public_id = str(kwargs.get('public_id'))

        post_content = request.data.get('content')

        if not post_content:
            return Response({ 'error': 'Não é permitido comentários em branco.' }, status=status.HTTP_400_BAD_REQUEST)
        
        use_case = CreatePostCommentUseCase(PostCommentRepository(), PostRepository(), UserProfileRepository())
        try:
            post_comment = use_case.execute(profile_id, public_id, post_content)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_comment_serialized = PostCommentSerializer(post_comment)
        body = post_comment_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)

    def get(self, request: Dict[str, Any], *args, **kwargs):

        public_id = str(kwargs.get('public_id'))

        use_case = ListPostCommentsUseCase(PostCommentRepository(), PostRepository())
        try:
            post_comments = use_case.execute(public_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)

        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_comments_serialized = PostCommentSerializer(post_comments, many=True)
        body = post_comments_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

class UpdateAndDeletePostCommentView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request: Dict[str, Any], *args, **kwargs):
        
        profile_id = request.user.profile.id
        comment_id = kwargs.get('comment_id')
        post_content = request.data.get('content')

        if not post_content:
            return Response({ 'error': 'Não é permitido comentários em branco.' }, status=status.HTTP_400_BAD_REQUEST)

        use_case = UpdatePostCommentUseCase(PostCommentRepository(), UserProfileRepository())
        try:
            post_comment_updated = use_case.execute(profile_id, comment_id, post_content)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except ForbiddenException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_403_FORBIDDEN)

        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_comment_serialized = PostCommentSerializer(post_comment_updated)
        body = post_comment_serialized.data

        return Response(body, status=status.HTTP_200_OK)

    def delete(self, request: Dict[str, Any], *args, **kwargs):
        
        profile_id = request.user.profile.id
        comment_id = kwargs.get('comment_id')

        use_case = DeletePostCommentUseCase(PostCommentRepository(), UserProfileRepository())
        try:
            use_case.execute(profile_id, comment_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)

        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
