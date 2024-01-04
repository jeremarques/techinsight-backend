from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.user_profile_views import GetAndUpdateCurrentUserProfileView, GetUserProfileView
from api.views.relationship_views import CreateFollowView, DeleteFollowView
from api.views.post_tag_views import CreatePostTagView, GetPostTagView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()), # work
    path('users/<str:username>/', GetUserView.as_view()), # work
    path('users/<int:user_id>/profile/', GetUserProfileView.as_view()), # work
    path('users/<int:user_id>/follow/', CreateFollowView.as_view()),
    path('users/<int:user_id>/unfollow/', DeleteFollowView.as_view()),
    # path('users/profiles/<int:profile_id>/posts'),
    path('me/', GetAndUpdateCurrentUserView.as_view()), # work
    path('me/profile/', GetAndUpdateCurrentUserProfileView.as_view()), # work
    # path('me/profile/posts/'),
    # path('posts/<uuid:post_id>/'),
    # path('posts/<uuid:post_id>/like/'),
    # path('posts/<uuid:post_id>/comments/'),
    # path('posts/<uuid:post_id>/comments/<int:comment_id>/'),
    path('tags/', CreatePostTagView.as_view()), # work
    path('tags/<slug:tag_slug>/', GetPostTagView.as_view()), # work
    # path('tags/<slug:tag_slug>/posts/'),
]