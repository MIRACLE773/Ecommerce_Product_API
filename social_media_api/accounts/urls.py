from django.urls import path
from .views import UserView, FollowUserView, UnfollowUserView

urlpatterns = [
    path("me/", UserView.as_view(), name="user-detail"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]