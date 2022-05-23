from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review
from .comment import CommentSerializer
from movies.models import Movie

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('__all__')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'rank', 'comments', 'movie', 'like_users', 'created_at', 'updated_at')


# Review List Read
class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('__all__')

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    # queryset annotate (views에서 채워줄것!)
    comment_count = serializers.IntegerField()
    like_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'rank', 'movie', 'comment_count', 'like_count')