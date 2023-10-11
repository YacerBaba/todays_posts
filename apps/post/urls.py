from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', login_required(HomeView.as_view(), login_url='login'), name='home-view'),
    path('home/', login_required(HomeView.as_view(), login_url='login')),
    path('create-post', views.create_post, name='create-post-view'),
    path('delete-post', views.delete_post)
]
