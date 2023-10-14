from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.post.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined']


class PostSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        self.fields['author'] = UserSerializer()
        return super(PostSerializer, self).to_representation(instance)

    class Meta:
        model = Post
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)

    def create(self, validated_data):
        password = validated_data['password']
        try:
            password_validation.validate_password(password=password)
        except password_validation.ValidationError as e:
            raise serializers.ValidationError(detail={'detail': e.messages})

        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
