from typing import Dict, Any
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.post import CreatePostUseCase, GetPostUseCase, ListPostsUseCase, UpdatePostUseCase, DeletePostUseCase
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.infrastructure.adapters.serializers.post_serializers import PostReadSerializer, PostCreateSerializer, PostUpdateSerializer
from api.errors import NotFoundException, ForbiddenException


class GetPostView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        public_id = kwargs.get('public_id')

        use_case = GetPostUseCase(PostRepository())

        try:
            post = use_case.execute(public_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        post_serialized = PostReadSerializer(post)
        body = post_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

class ListPostsView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        profile_id = kwargs.get('profile_id')

        use_case = ListPostsUseCase(PostRepository(), UserProfileRepository())

        try:
            posts = use_case.execute(profile_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        posts_serialized = PostReadSerializer(posts, many=True)
        body = posts_serialized.data

        return Response(body, status=status.HTTP_200_OK)


class CreateCurrentUserPostView(APIView):

    def post(self, request: Dict[str, Any], *args, **kwargs):
        user = request.user
        data = {
            'title': request.data.get('title'),
            'slug': slugify(request.data.get('title')),
            'content': request.data.get('content'),
            'tag_id': request.data.get('tag_id')
        }
        validate_data = PostCreateSerializer(data=data)

        if not validate_data.is_valid():
            return Response({ 'error': validate_data.errors }, status=status.HTTP_400_BAD_REQUEST)
        
        use_case = CreatePostUseCase(PostRepository(), UserProfileRepository(), PostTagRepository())
        try:
            post = use_case.execute(user.id, data.get('title'), data.get('slug'), data.get('content'), data.get('tag_id'))
        
        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_serialized = PostReadSerializer(post)
        body = post_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
        

class UpdateAndDeleteCurrentUserPostView(APIView):
    def put(self, request: Dict[str, Any], *args, **kwargs):
        profile_id = request.user.profile.id
        post_id = kwargs.get('post_id')
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content')
        }
        validate_data = PostUpdateSerializer(data=data)

        if not validate_data.is_valid():
            return Response({ 'error': validate_data.errors })
        
        use_case = UpdatePostUseCase(PostRepository())

        try:
            updated_post = use_case.execute(profile_id, post_id, data.get('title'), data.get('content'))

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except ForbiddenException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_403_FORBIDDEN)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        updated_post_serialized = PostReadSerializer(updated_post)
        body = updated_post_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    
    def delete(self, request: Dict[str, Any], *args, **kwargs):
        profile_id = request.user.profile.id
        post_id = kwargs.get('post_id')

        use_case = DeletePostUseCase(PostRepository())
        try:
            use_case.execute(profile_id, post_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except ForbiddenException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_403_FORBIDDEN)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

