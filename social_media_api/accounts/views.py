from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from .models import CustomUser
from rest_framework import generics, status, permissions


class UserView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [ IsAuthenticated]

    def get(self,request):
        return request({"message": f"Hello{request.user.username}, you are authenticated!"})
    

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
  

    def post(self, request, user_id):
        """Authenticated user follows another user"""
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=200)


class UnfollowUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        """Authenticated user unfollows another user"""
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself."}, status=400)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=200)