from django.urls import path
from api.views.user_view import UserView

urlpatterns = [
    path('users/', UserView.as_view())
]