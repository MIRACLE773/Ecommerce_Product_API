from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CustomAuthToken

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('token/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('', include(router.urls)),
]
