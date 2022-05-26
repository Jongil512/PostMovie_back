import requests
import json

TMDB_API_KEY = '0cbbb073b67ccb4d98dfbe150348cc79'

def get_movie_datas():
    total_data = []

    for i in range(1, 12):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{movie['poster_path']}",
                    'genres': movie['genre_ids'],
                    'vote_count': movie['vote_count'],
                    'rate_average' : 0
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)

def get_genre_data():
    total_data = []

    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()

    for genre in genres['genres']:
        fields = {
            # 'genre_id': genre['id'],
            'name': genre['name'],
        }

        data = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
        total_data.append(data)

    with open("movies/fixtures/genre_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=4, ensure_ascii=False)


get_movie_datas()
get_genre_data()

'''
movies/fixtures/ 만들고 실행
장르부터 먼저 실행 주의

python manage.py loaddata genre_data.json
python manage.py loaddata movie_data.json

'''