from django.urls import path
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.user_profile_views import GetAndUpdateCurrentUserProfileView, GetUserProfileView
from api.views.relationship_views import CreateFollowView, DeleteFollowView
from api.views.post_tag_views import CreatePostTagView, GetPostTagView
from api.views.post_views import  GetPostView, ListProfilePostsView, ListPostsByTagView, CreateCurrentUserPostView, UpdateAndDeleteCurrentUserPostView
from api.views.post_like_views import CreateAndDeletePostLikeView
from api.views.post_comment_views import ListCreatePostCommentView, UpdateAndDeletePostCommentView

urlpatterns = [
    path('users/register/', CreateUserView.as_view()), # work
    path('users/<str:username>/', GetUserView.as_view()), # work
    path('users/<str:username>/profile/', GetUserProfileView.as_view()), # work
    path('users/<int:user_id>/follow/', CreateFollowView.as_view()), # work
    path('users/<int:user_id>/unfollow/', DeleteFollowView.as_view()), # work
    path('users/profiles/<int:profile_id>/posts/', ListProfilePostsView.as_view()), # work
    path('me/', GetAndUpdateCurrentUserView.as_view()), # work
    path('me/profile/', GetAndUpdateCurrentUserProfileView.as_view()), # work
    path('me/posts/', CreateCurrentUserPostView.as_view()), # work
    path('me/posts/<str:post_id>/', UpdateAndDeleteCurrentUserPostView.as_view()), # work
    path('posts/<str:public_id>/', GetPostView.as_view()), # work
    path('posts/<str:post_id>/likes/', CreateAndDeletePostLikeView.as_view()), # work
    path('posts/<str:post_id>/comments/', ListCreatePostCommentView.as_view()), # work
    path('posts/comments/<int:comment_id>/', UpdateAndDeletePostCommentView.as_view()), # work
    path('tags/', CreatePostTagView.as_view()), # work
    path('tags/<slug:tag_slug>/', GetPostTagView.as_view()), # work
    path('tags/<slug:tag_slug>/posts/', ListPostsByTagView.as_view()) # work
]