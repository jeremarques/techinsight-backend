from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.user_views import GetAndUpdateCurrentUserView, CreateUserView, GetUserView
from api.views.user_profile_views import GetAndUpdateCurrentUserProfileView, GetUserProfileView
from api.views.relationship_views import CreateFollowView, DeleteFollowView
from api.views.post_tag_views import ListCreatePostTagView, GetPostTagView
from api.views.post_views import  GetPostView, ListProfilePostsView, ListAllPostsView, ListPostsByTagView, CreateCurrentUserPostView, UpdateAndDeleteCurrentUserPostView
from api.views.post_like_views import CreateAndDeletePostLikeView
from api.views.post_comment_views import ListCreatePostCommentView, UpdateAndDeletePostCommentView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()), # work, any
    path('login/refresh/', TokenRefreshView.as_view()), # work, any
    path('register/', CreateUserView.as_view()), # work, any
    path('users/<str:username>/', GetUserView.as_view()), # work, any
    path('users/<str:username>/profile/', GetUserProfileView.as_view()), # work, any
    path('users/<int:user_id>/follow/', CreateFollowView.as_view()), # work, authenticated
    path('users/<int:user_id>/unfollow/', DeleteFollowView.as_view()), # work, authenticated
    path('users/profiles/<int:profile_id>/posts/', ListProfilePostsView.as_view()), # work, any
    path('me/', GetAndUpdateCurrentUserView.as_view()), # work, authenticated
    path('me/profile/', GetAndUpdateCurrentUserProfileView.as_view()), # work, authenticated
    path('me/posts/', CreateCurrentUserPostView.as_view()), # work, authenticated
    path('me/posts/<str:post_id>/', UpdateAndDeleteCurrentUserPostView.as_view()), # work, authenticated
    path('posts/', ListAllPostsView.as_view()), # work, any, temporaly
    path('posts/<str:public_id>/', GetPostView.as_view()), # work, any
    path('posts/<str:public_id>/likes/', CreateAndDeletePostLikeView.as_view()), # work, authenticated
    path('posts/<str:public_id>/comments/', ListCreatePostCommentView.as_view()), # work, any/authenticated
    path('posts/comments/<int:comment_id>/', UpdateAndDeletePostCommentView.as_view()), # work, authenticated
    path('tags/', ListCreatePostTagView.as_view()), # work, authenticated
    path('tags/<slug:tag_slug>/', GetPostTagView.as_view()), # work, any
    path('tags/<slug:tag_slug>/posts/', ListPostsByTagView.as_view()) # work, any
]
