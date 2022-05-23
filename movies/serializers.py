from rest_framework import serializers
from .models import Movie, Genre
from reviews.models import Review

class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('pk', 'name')


    class ReviewSerializer(serializers.ModelSerializer):
        
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
