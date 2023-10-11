from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, get_object_or_404, \
    RetrieveUpdateAPIView
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, DjangoObjectPermissions
from rest_framework.response import Response
from apis.serializers import PostSerializer, CustomSerializer
from apps.post import services
from apps.post.models import Post


class CustomModelPerms(DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        print("getting executed")
        if request.method == 'GET':
            return request.user == obj.author
        return False


class GetPostsView(viewsets.ModelViewSet):
    """
    This is posts view set
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = services.find_all()

    def get_queryset(self):
        user_id = self.request.user.id
        return services.get_posts_by_user_id(user_id)

    def get_object(self):
        pk = self.kwargs.get("pk")
        post = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(self.request, post)
        return post

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GetOnePost(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = services.find_all()
    lookup_field = "id"
    permission_classes = [CustomModelPerms]


class GetPostsViewSet(viewsets.ModelViewSet):
    dataset = services.find_all()
    authentication_classes = []
    permission_classes = []


class CreatePostView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [DjangoModelPermissions]


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status.HTTP_200_OK)




def route(request):
    first_name = "yacer"
    serializer = CustomSerializer({'first_name': first_name})
    print("serialized successfully")
    return Response(serializer.data)
