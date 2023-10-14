from django.urls import path, include

from apis.api_authentication import urls as auth_urls
from apis.api_post import urls as post_urls

urlpatterns = [
    path('', include(auth_urls)),
    path('', include(post_urls))
]
