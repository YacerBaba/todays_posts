from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserRegistrationSerializer


class RegisterUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(data={'error': 'will work ?'}, status=status.HTTP_200_OK)

    def post(self, request):
        reg_serializer = UserRegistrationSerializer(request.data)
        ser = reg_serializer.data
        # if reg_serializer.is_valid():
        # check user existence
        email = ser['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            return Response(data={'error': 'This email is already exist'}, status=status.HTTP_400_BAD_REQUEST)

        result = reg_serializer.save(commit=False)
        if result:
            return Response(data={'msg': 'user created successfully'}, status=status.HTTP_201_CREATED)
        # return Response(data=result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data=reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
