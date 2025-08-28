from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
      class Meta:
        models = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = '__all__'