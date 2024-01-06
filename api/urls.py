from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.user_profile_views import GetAndUpdateCurrentUserProfileView, GetUserProfileView
from api.views.relationship_views import CreateFollowView, DeleteFollowView
from api.views.post_tag_views import CreatePostTagView, GetPostTagView
from api.views.post_views import  GetPostView, ListPostsView, CreateCurrentUserPostView, UpdateAndDeleteCurrentUserPostView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()), # work
    path('users/<str:username>/', GetUserView.as_view()), # work
    path('users/<str:username>/profile/', GetUserProfileView.as_view()), # work
    path('users/<int:user_id>/follow/', CreateFollowView.as_view()), # work
    path('users/<int:user_id>/unfollow/', DeleteFollowView.as_view()), # work
    path('users/profiles/<int:profile_id>/posts/', ListPostsView.as_view()), # work
    path('me/', GetAndUpdateCurrentUserView.as_view()), # work
    path('me/profile/', GetAndUpdateCurrentUserProfileView.as_view()), # work
    path('me/posts/', CreateCurrentUserPostView.as_view()), # work
    path('me/posts/<str:post_id>/', UpdateAndDeleteCurrentUserPostView.as_view()), # work
    path('posts/<str:public_id>/', GetPostView.as_view()), # work
    # path('posts/<uuid:post_id>/like/'),
    # path('posts/<uuid:post_id>/comments/'),
    # path('posts/<uuid:post_id>/comments/<int:comment_id>/'),
    path('tags/', CreatePostTagView.as_view()), # work
    path('tags/<slug:tag_slug>/', GetPostTagView.as_view()), # work
    # path('tags/<slug:tag_slug>/posts/'),
]