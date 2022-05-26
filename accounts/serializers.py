from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.models import Review, Comment
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'title')
    
    class CommentSerializer(serializers.ModelSerializer):

        class ReviewSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Review
                fields = ('pk', 'title')

        review = ReviewSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('pk', 'content', 'review')

    class UserSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    like_reviews = ReviewSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True)
    comments = CommentSerializer(many=True)
    followers = UserSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_reviews', 'reviews', 'comments', 'followers', 'followings', 'wishlist')