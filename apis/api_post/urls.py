from django.urls import path

from apis.api_post.views import GetPostsView, GetOnePost, CreatePostView

urlpatterns = [
    path('posts/', GetPostsView.as_view(), name='get-posts-view'),
    path('posts/<int:id>', GetOnePost.as_view(), name='get-post-view'),
    path('posts/create', CreatePostView.as_view(), name='create-post-view'),
]
