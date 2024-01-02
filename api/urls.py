from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()),
    path('me/', GetAndUpdateCurrentUserView.as_view()),
]