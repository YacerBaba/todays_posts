from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetPostsView

router = DefaultRouter()
router.register('', GetPostsView, basename='testing_bname')

urlpatterns = [
    path('', include(router.urls))
]