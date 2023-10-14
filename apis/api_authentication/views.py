from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apis.serializers import UserRegistrationSerializer


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
