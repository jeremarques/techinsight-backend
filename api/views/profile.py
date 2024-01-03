from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.domain.use_cases.profile import GetProfileUseCase
from api.infrastructure.adapters.repositories.profile import ProfileRepository
from api.infrastructure.adapters.serializers.profile_serializers import ProfileReadSerializer
from api.errors import NotFoundException

class GetCurrentUserProfileView(APIView):

    def get(self, request: Dict[str, Any], *args, **kwargs):
        user_id = request.user.id
        user_case = GetProfileUseCase(ProfileRepository())

        try:
            current_user_profile = user_case.execute(user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        current_user_profile_serialized = ProfileReadSerializer(current_user_profile)
        body = current_user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)
    

class GetUserProfileView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        user_id = kwargs.get('user_id')
        user_case = GetProfileUseCase(ProfileRepository())

        try:
            current_user_profile = user_case.execute(user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        current_user_profile_serialized = ProfileReadSerializer(current_user_profile)
        body = current_user_profile_serialized.data

        return Response(body, status=status.HTTP_200_OK)