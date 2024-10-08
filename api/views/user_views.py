from typing import Dict, Any
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.domain.use_cases.user import GetUserUseCase, CreateUserUseCase, UpdateUserUseCase
from api.infrastructure.adapters.repositories.user import UserRepository
from api.infrastructure.adapters.repositories.user_profile import UserProfileRepository
from api.infrastructure.adapters.serializers.user_serializers import UserReadSerializer, UserCreateSerializer, UserEditSerializer
from api.errors import NotFoundException, AlreadyExistsException, UsernameAlreadyExistsException, EmailAlreadyExistsException

class GetAndUpdateCurrentUserView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request: Dict[str, Any], *args, **kwargs):
        user = request.user
        use_case = GetUserUseCase(UserRepository())

        try:    
            user = use_case.execute(user.username, None)
        
        except NotFoundException as err:
            return Response({'error': str(err)}, status=status.HTTP_404_NOT_FOUND)

        serialized_user = UserReadSerializer(user)
        body = serialized_user.data

        return Response(body, status=status.HTTP_200_OK)
    

    def put(self, request: Dict[str, Any], *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({'message': 'Usuário não autenticado.'}, status=status.HTTP_401_UNAUTHORIZED)

        use_case = UpdateUserUseCase(UserRepository())
        update_user_data = {
            'username': user.username,
            'new_username': request.data.get('username'),
            'email': request.data.get('email'),
            'full_name': request.data.get('full_name')
        }
        data = UserEditSerializer(data=update_user_data)
        
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            updated_user = use_case.execute(
                id=user.id,
                username=request.data.get('username'),
                email=request.data.get('email'),
                full_name=request.data.get('full_name')
            )
            
        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        except AlreadyExistsException as err:
            return Response({
                'username': ['O nome de usuário já existe.'],
                'email': ['O e-mail já existe.']
            }, status=status.HTTP_400_BAD_REQUEST)        
        
        except UsernameAlreadyExistsException as err:
            return Response({ 'username': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except EmailAlreadyExistsException as err:
            return Response({ 'email': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        updated_user_serialized = UserReadSerializer(updated_user)
        body = updated_user_serialized.data

        return Response(body, status=status.HTTP_200_OK)
        

class CreateUserView(APIView):
        
    permission_classes = [AllowAny]

    def post(self, request: Dict[str, Any], *args, **kwargs):
        data = UserCreateSerializer(data=request.data)
        use_case = CreateUserUseCase(UserRepository(), UserProfileRepository())
        
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = use_case.execute(
                username=request.data.get('username'),
                password=request.data.get('password'),
                email=request.data.get('email'),
                full_name=request.data.get('full_name')
            )

        except AlreadyExistsException as err:
            return Response({
                'username': ['O nome de usuário já existe.'],
                'email': ['O e-mail já existe.']
            }, status=status.HTTP_400_BAD_REQUEST)        
        
        except UsernameAlreadyExistsException as err:
            return Response({ 'username': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except EmailAlreadyExistsException as err:
            return Response({ 'email': str(err) }, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            return Response({ 'error': str(err) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        user_serialized = UserReadSerializer(user)
        body = user_serialized.data

        return Response(body, status=status.HTTP_201_CREATED)
    

class GetUserView(APIView):

    permission_classes = [AllowAny]

    def get(self, request: Dict[str, Any], *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id = None

        username = str(kwargs.get('username'))
        use_case = GetUserUseCase(UserRepository())
        
        try:
            user = use_case.execute(username, user_id)

        except NotFoundException as err:
            return Response({ 'error': str(err) }, status=status.HTTP_404_NOT_FOUND)
        
        user_serialized = UserReadSerializer(user)
        body = user_serialized.data

        return Response(body, status=status.HTTP_200_OK)
