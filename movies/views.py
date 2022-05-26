from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Movie
from reviews.models import Review
from .serializers import MovieSerializer, MovieListSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_recommend(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    recommended = []
    reviews = movie.reviews.all()
    for review in reviews:
        user = review.user
        reviews2 = user.reviews.all()
        for review2 in reviews2:
            rec_movie = review2.movie
            if rec_movie.pk not in recommended:
                recommended.append(rec_movie.pk)
    context = {
        'recommended' : recommended
    }
    return Response(context, status=status.HTTP_200_OK)