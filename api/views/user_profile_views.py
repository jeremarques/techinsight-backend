from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.domain.use_cases.user_profile import GetUserProfileUseCase, UpdateUserProfileUseCase
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.serializers.user_profile_serializers import UserProfileReadSerializer, UserProfileCreateSerializer
from api.errors import NotFoundException
    

class GetUserProfileView(APIView):

    permission_classes = [AllowAny]

    def get(self, request: Dict[str, Any], *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = None

        username = kwargs.get('username')
        user_case = GetUserProfileUseCase(UserProfileRepository(), UserRepository())

        try:
            user_profile = user_case.execute(username, user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        user_profile_serialized = UserProfileReadSerializer(user_profile)
        body = user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

class GetAndUpdateCurrentUserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request: Dict[str, Any], *args, **kwargs):
        user_id = request.user.username
        user_case = GetUserProfileUseCase(UserProfileRepository(), UserRepository())

        try:
            current_user_profile = user_case.execute(user_id, None)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        current_user_profile_serialized = UserProfileReadSerializer(current_user_profile)
        body = current_user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

    def put(self, request: Dict[str, Any], *args, **kwargs):
        user_id = request.user.id
        use_case = UpdateUserProfileUseCase(UserProfileRepository(), UserRepository())

        validate_data = UserProfileCreateSerializer(data=request.data)

        if not validate_data.is_valid():
            return Response({ 'error': validate_data.errors }, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile_updated_entity = use_case.execute(
                user_id,
                validate_data.validated_data.get('name') or "",
                validate_data.validated_data.get('profile_photo') or "",
                validate_data.validated_data.get('website_url') or "",
                validate_data.validated_data.get('bio') or "",
                validate_data.validated_data.get('about') or "",
                validate_data.validated_data.get('date_of_birth')
            )

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        profile_updated_serialized = UserProfileReadSerializer(profile_updated_entity)
        body = profile_updated_serialized.data

        return Response(body, status=status.HTTP_200_OK)
