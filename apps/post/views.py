from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from apps.post import services
from apps.post.forms import CreatePostForm
from apps.post.models import Post
from .templates import *


# Create your views here.

class HomeView(ListView):
    model = Post
    queryset = Post.objects.get_posts_with_authors()
    template_name = 'templates/home.html'
    context_object_name = 'posts'


@login_required(login_url='/login')
@require_http_methods(['POST', 'GET'])
@permission_required('post.add_post', login_url='/login', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            author = request.user
            request.user.has_perm('')
            post = form.save(commit=False)
            post.author = author
            post.save()
            return redirect('/home')
        else:
            return render(request, 'create_post.html', {"form": form})
    else:
        form = CreatePostForm()
        return render(request, 'apps/post/templates/create_post.html', {"form": form})


@require_http_methods(['POST'])
def delete_post(request):
    post_id = request.POST['post-id']
    post = services.get_post_by_id(post_id)
    if post.author == request.user or request.user.has_perm('post.delete_post'):
        result = Post.objects.filter(pk=post_id).delete()
        if not result:
            print('failed')
    return redirect('/home')
