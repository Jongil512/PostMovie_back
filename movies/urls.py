from django.contrib import admin
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.get_movie_list, name='movies'),
    path('<int:movie_pk>/', views.movie_detail, name='detail'),
    path('<int:movie_pk>/recommend/', views.movie_recommend, name='recommend'),
]
