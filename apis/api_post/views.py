from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import DjangoModelPermissions, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from apis.serializers import PostSerializer
from apps.post.models import Post


class GetPostsView(ListAPIView):
    authentication_classes = []
    queryset = Post.objects.get_posts_ordered_by_date()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class GetOnePost(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [DjangoModelPermissions]

    def get_object(self):
        id = self.kwargs['id']
        post = get_object_or_404(self.get_queryset(), pk=id)
        self.check_object_permissions(self.request, post)
        return post


class CreatePostView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [DjangoModelPermissions]

