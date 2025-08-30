from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# We are creating a custom User model by extending AbstractUser
# This allows us to add/modify fields in Django's default User
class User(AbstractUser):
    # Making email unique so no two users can register with the same email
    email = models.EmailField(unique=True)

    # Automatically store the date and time the user joined
    date_joined = models.DateTimeField(auto_now_add=True)

    # ---- FIXING ManyToMany RELATIONSHIP CLASHES ----
    # Django's default User already has groups & permissions
    # but when we extend it, we must rename them to avoid conflicts

    # Groups = collection of users with the same permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',      # Renamed to avoid clash with default 'user_set'
        related_query_name='custom_user',    # Used in queries, e.g. group.custom_user.all()
        blank=True,                          # Field is optional
        help_text='The groups this user belongs to.',  # Shown in admin
        verbose_name='groups',               # Display name in admin
    )

    # User-specific permissions
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',   # Renamed to avoid clash
        related_query_name='custom_user_permissions', # For queries
        blank=True,
        help_text='Specific permissions for this user.', 
        verbose_name='user permissions',
    )

    # String representation of the user (how it will show in admin panel)
    def __str__(self):
        return self.username

    # Making email unique so no two users can register with the same email
    email = models.EmailField(unique=True)

    # Automatically store the date and time the user joined
    date_joined = models.DateTimeField(auto_now_add=True)

    # ---- FIXING ManyToMany RELATIONSHIP CLASHES ----
    # Django's default User already has groups & permissions
    # but when we extend it, we must rename them to avoid conflicts

    # Groups = collection of users with the same permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',      # Renamed to avoid clash with default 'user_set'
        related_query_name='custom_user',    # Used in queries, e.g. group.custom_user.all()
        blank=True,                          # Field is optional
        help_text='The groups this user belongs to.',  # Shown in admin
        verbose_name='groups',               # Display name in admin
    )

    # User-specific permissions
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',   # Renamed to avoid clash
        related_query_name='custom_user_permissions', # For queries
        blank=True,
        help_text='Specific permissions for this user.', 
        verbose_name='user permissions',
    )

    # String representation of the user (how it will show in admin panel)
    def __str__(self):
        return self.username