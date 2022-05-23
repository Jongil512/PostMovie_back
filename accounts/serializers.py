from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.models import Review, Comment

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

    like_reviews = ReviewSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email', 'like_reviews', 'reviews', 'comments')

