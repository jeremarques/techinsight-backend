from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.user_profile import GetUserProfileUseCase, UpdateUserProfileUseCase
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.serializers.user_profile_serializers import UserProfileSerializer, UserProfileCreateSerializer
from api.errors import NotFoundException
    

class GetUserProfileView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        user_id = kwargs.get('user_id')
        user_case = GetUserProfileUseCase(UserProfileRepository())

        try:
            current_user_profile = user_case.execute(user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        current_user_profile_serialized = UserProfileSerializer(current_user_profile)
        body = current_user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

class GetAndUpdateCurrentUserProfileView(APIView):

    def get(self, request: Dict[str, Any], *args, **kwargs):
        user_id = request.user.id
        user_case = GetUserProfileUseCase(UserProfileRepository())

        try:
            current_user_profile = user_case.execute(user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        current_user_profile_serialized = UserProfileSerializer(current_user_profile)
        body = current_user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

    def put(self, request: Dict[str, Any], *args, **kwargs):
        user_id = request.user.id
        use_case = UpdateUserProfileUseCase(UserProfileRepository())

        data = UserProfileCreateSerializer(data=request.data)
        if not data.is_valid():
            return Response({ 'error': data.errors }, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile_updated_entity = use_case.execute(
                user_id,
                data.validated_data.get('name'),
                data.validated_data.get('profile_photo'),
                data.validated_data.get('website_url'),
                data.validated_data.get('bio'),
                data.validated_data.get('about'),
                data.validated_data.get('date_of_birth')
            )

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        profile_updated_serialized = UserProfileSerializer(profile_updated_entity)
        body = profile_updated_serialized.data

        return Response(body, status=status.HTTP_200_OK)