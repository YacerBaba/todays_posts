from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, EmailField, CharField, ModelForm

from apps.post.models import Post


class RegistrationForm(UserCreationForm):
    first_name = CharField(label="First name", max_length=150, required=True)
    last_name = CharField(label="Last name", max_length=150, required=True)
    email = EmailField(label="Email address", required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        is_email_exist = User.objects.filter(email=email).exists()
        if is_email_exist:
            raise forms.ValidationError('This email is already exist')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
