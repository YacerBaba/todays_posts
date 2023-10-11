from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Model
from rest_framework.decorators import api_view


# Create your models here.

class PostManager(models.Manager):
    def get_posts_ordered_by_date(self):
        return self.all().order_by('-updated_at')

    def get_posts_with_authors(self):
        return self.all().select_related('author').order_by('-updated_at')

    def get_posts_by_user_id(self, post_id):
        return self.all().filter(author_id=post_id)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = PostManager()

    class Meta:
        db_table = 'posts'
