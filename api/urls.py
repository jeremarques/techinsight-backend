from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.user_profile_views import GetAndUpdateCurrentUserProfileView, GetUserProfileView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()), # work
    path('users/<str:username>/', GetUserView.as_view()), # work
    path('users/<int:user_id>/profile/', GetUserProfileView.as_view()), # work
    # path('users/<int:user_id>/follow/'),
    # path('users/<int:user_id>/unfollow/'),
    # path('users/profiles/<int:profile_id>/posts'),
    path('me/', GetAndUpdateCurrentUserView.as_view()), # work
    path('me/profile/', GetAndUpdateCurrentUserProfileView.as_view()), # work
    # path('me/profile/posts/'),
    # path('posts/<uuid:post_id>/'),
    # path('posts/<uuid:post_id>/like/'),
    # path('posts/<uuid:post_id>/comments/'),
    # path('posts/<uuid:post_id>/comments/<int:comment_id>/'),
    # path('tags/<slug:tag_slug>/'),
]