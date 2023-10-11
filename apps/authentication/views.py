from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from apps.authentication import services
from apps.post.forms import RegistrationForm


# Create your views here.

class SignupView(View):
    @staticmethod
    def get(request):
        registration = RegistrationForm()
        return render(request, 'registration/sign_up.html', {"form": registration})

    @staticmethod
    def post(request):
        registered_user = RegistrationForm(request.POST)
        if registered_user.is_valid():
            first_name = registered_user.cleaned_data['first_name']
            last_name = registered_user.cleaned_data['last_name']
            email = registered_user.cleaned_data['email']
            password = registered_user.cleaned_data['password1']
            user = services.save_user(first_name, last_name, email, password)
            login(request, user)
            return HttpResponseRedirect(reverse('home-view'))
        else:
            return render(request, 'registration/sign_up.html', {"form": registered_user})
