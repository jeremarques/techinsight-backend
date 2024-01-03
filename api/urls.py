from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.profile import GetCurrentUserProfileView, GetUserProfileView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()),
    path('users/<str:username>/', GetUserView.as_view()),
    path('users/<int:user_id>/profile/', GetUserProfileView.as_view()),
    path('me/', GetAndUpdateCurrentUserView.as_view()),
    path('me/profile/', GetCurrentUserProfileView.as_view()),
]