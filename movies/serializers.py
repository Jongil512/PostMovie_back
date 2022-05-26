from rest_framework import serializers
from .models import Movie, Genre
from django.contrib.auth import get_user_model
from reviews.models import Review

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk', 'name')


    class ReviewSerializer(serializers.ModelSerializer):
        
        class UserSerializer(serializers.ModelSerializer):

            class Meta:
                model = User
                fields = ('pk', 'username')

        user = UserSerializer(read_only=True)
        
        class Meta:
            model = Review
            fields = ('__all__')

    genres = GenreSerializer(many=True)
    reviews = ReviewSerializer(many=True)


    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk', 'name')
            
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
