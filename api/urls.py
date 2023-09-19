from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import GetPostsView, GetOnePost, CreatePostView, get_posts, RegisterUserView

urlpatterns = [
    path('posts', GetPostsView.as_view(), name='get-posts-view'),
    path('posts/<int:id>', GetOnePost.as_view(), name='get-post-view'),
    path('posts/create', CreatePostView.as_view(), name='create-post-view'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterUserView.as_view(), name='register-user-view')
]
