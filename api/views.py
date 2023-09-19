from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.db.models import QuerySet
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404, \
    RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import PostSerializer, UserRegistrationSerializer
from post.models import Post
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, AllowAny, IsAdminUser


class CustomModelPerms(DjangoModelPermissions):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class GetPostsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Post.objects.get_posts_ordered_by_date()
    serializer_class = PostSerializer
    permission_classes = [DjangoModelPermissions]


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


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


class RegisterUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        return Response(data='will work ?', status=status.HTTP_200_OK)

    def post(self, request):
        reg_serializer = UserRegistrationSerializer(data=request.data)
        if reg_serializer.is_valid():
            # check user existence
            email = reg_serializer.validated_data['email']
            qs = User.objects.filter(email=email)
            if qs.exists():
                return Response(data='This email is already exist', status=status.HTTP_400_BAD_REQUEST)

            result = reg_serializer.save()
            if result:
                return Response(data={'msg': 'user created successfully'}, status=status.HTTP_201_CREATED)
            return Response(data=result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
