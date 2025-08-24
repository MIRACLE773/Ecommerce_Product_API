# urls.py

# Import the admin site
from django.contrib import admin  

# Import path function to define URL patterns
from django.urls import path  

# Import Django's built-in authentication views (for login/logout)
from django.contrib.auth import views as auth_views  

# Import views from this app
from . import views  

# Import specific views for post search and comment operations
from .views import post_search, CommentCreateView, CommentUpdateView, CommentDeleteView  

# Define all the URL routes of your app
urlpatterns = [
    # Login page (uses Django's built-in LoginView with a custom template)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout page (uses Django's built-in LogoutView with a custom template)
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # User registration (custom view you created in views.py)
    path('register/', views.register, name='register'),

    # User profile page (custom view)
    path('profile/', views.profile, name='profile'),

    # List of all posts (uses PostListView class)
    path('posts/', views.PostListView.as_view(template_name='blog/post_list.html'), name='post-list'),

    # Detailed view of a single post (pk = primary key of post)
    path('post/<int:pk>/', views.PostDetailView.as_view(template_name='blog/post_detail.html'), name='post-detail'),

    # Create a new comment for a specific post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    # Update an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),

    # Delete an existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Create a new blog post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),

    # Update an existing blog post
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),

    # Delete a blog post (custom delete confirmation template is used)
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(template_name='blog/post_confirm_delete.html'), name='post-delete'),

    # Search posts
    path('search/', post_search, name='post-search'),

    # Search posts by tag name (string version of tag)
    path('tags/<str:tag_name>/', post_search, name='tag-detail'),

    # Search posts by tag slug (URL-friendly version of tag)
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
