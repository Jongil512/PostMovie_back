from telnetlib import STATUS
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer
from rest_framework import status
from movies.models import Movie

User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, username):
    guest = request.user
    user = get_object_or_404(get_user_model(), username=username)

    if guest != user:
        if user.followers.filter(pk=guest.pk).exists():
            user.followers.remove(guest)
        else:
            user.followers.add(guest)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def wishlist(request, movie_pk):
    username = request.user.username
    user = get_object_or_404(get_user_model(), username=username)
    if user.wishlist.filter(pk=movie_pk).exists():
        user.wishlist.remove(movie_pk)
    else:
        user.wishlist.add(movie_pk)  
    serializers = ProfileSerializer(user)
    return Response(serializers.data, status=status.HTTP_200_OK)