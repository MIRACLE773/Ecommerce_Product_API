from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    register_view, profile_view, profile_update_view,
    BlogPostListView, BlogPostCreateView, BlogPostDeleteView,
    BlogPostDetailView, BlogPostUpdateView, BlogCommentCreateView,
    BlogCommentUpdateView, BlogCommentDeleteView,
    SearchView, TagView
)

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
    path('register/', register_view, name='register'),

    # Profile
    path('profile/', profile_view, name='profile'),
    path('profile-update/', profile_update_view, name='profile-updates'),

    # Blog posts
    path('post/', BlogPostListView.as_view(), name='post-list'),
    path('post/new/', BlogPostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', BlogCommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', BlogCommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', BlogCommentDeleteView.as_view(), name='comment-delete'),

    # Search and tags
    path('search/', SearchView.as_view(), name='search'),
    path('tags/<slug:tag_name>/', TagView.as_view(), name='tag-posts'),
]
