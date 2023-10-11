from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .post import urls as post_urls
from .authentication import urls as auth_urls

urlpatterns = [
    path('posts/', include(post_urls)),
    path('',include(auth_urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
