from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostCreateView, CommentCreateView, UserFeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostCreateView, basename='post')
router.register(r'comments', CommentCreateView, basename='comment')
urlpatterns = router.urls


urlpatterns = [
  path('feed/', UserFeedView.as_view(), name='feed'),
  path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
  path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
] + router.urls