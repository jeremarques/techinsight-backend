from typing import Dict, Any
from django.utils.text import slugify
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.post_tag import CreatePostTagUseCase, GetPostTagUseCase
from api.infrastructure.adapters.repositories.post_tag import PostTagRepository
from api.infrastructure.adapters.serializers.post_tag_serializers import PostTagSerializer
from api.errors import NotFoundException, AlreadyExistsException


class CreatePostTagView(APIView):

    def post(self, request: Dict[str, Any], *args, **kwargs):

        data = {
            'name': request.data.get('name'),
            'slug': slugify(request.data.get('name'))
        }
        validate_data = PostTagSerializer(data=data)

        if not validate_data.is_valid():
            return Response({ 'error': validate_data.errors }, status=status.HTTP_400_BAD_REQUEST)
        
        use_case = CreatePostTagUseCase(PostTagRepository())
        try:
            post_tag = use_case.execute(data.get('name'), data.get('slug'))
        
        except AlreadyExistsException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        post_tag_serialized = PostTagSerializer(post_tag)
        body = post_tag_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
        

class GetPostTagView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        tag_slug = kwargs.get('tag_slug')
        use_case = GetPostTagUseCase(PostTagRepository())

        try:
            post_tag = use_case.execute(tag_slug)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        post_tag_serialized = PostTagSerializer(post_tag)
        body = post_tag_serialized.data

        return Response(body, status=status.HTTP_200_OK)
