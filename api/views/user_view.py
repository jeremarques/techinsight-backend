from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework.response import Response
from api.domain.use_cases.user import ListUsersUseCase
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.serializers.user_serializers import PublicUserReadSerializer

class UserView(APIView):
    def get(self, request: Dict[str, Any], *args, **kwargs):
        use_case = ListUsersUseCase(UserRepository())
        users_list = use_case.execute()
        serialized_users = PublicUserReadSerializer(users_list, many=True)
        body = serialized_users.data
        status = 200

        return Response(body, status)
        

    def post(self, request, *args, **kwargs):
        ...
