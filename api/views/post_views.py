from typing import Dict, Any
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.post import CreatePostUseCase, GetPostUseCase
from api.infrastructure.adapters.repositories.post import PostRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.infrastructure.adapters.serializers.post_serializers import PostReadSerializer, PostCreateSerializer
from api.errors import NotFoundException


class GetAndCreateCurrentUserPostView(APIView):

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
        
        post_serialized = PostReadSerializer(post)
        body = post_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
    
    # def get(self, request: Dict[str, Any], *args, **kwargs):
    #     tag_slug = kwargs.get('tag_slug')
    #     use_case = GetPostTagUseCase(PostTagRepository())

    #     try:
    #         post_tag = use_case.execute(tag_slug)

    #     except NotFoundException as err:
    #         return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
    #     post_tag_serialized = PostTagSerializer(post_tag)
    #     body = post_tag_serialized.data

    #     return Response(body, status=status.HTTP_200_OK)
        

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