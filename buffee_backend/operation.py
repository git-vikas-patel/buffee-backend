import requests

def get_movie_names(api_key):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1"
    response = requests.get(url)
    data = response.json()
    movies = data['results']
    movie_names = [movie['title'] for movie in movies]
    return movie_names
