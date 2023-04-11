import requests
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

@csrf_exempt
def trending_movies(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    api_key = '6e65f8bcc3b3ca0c03e49fbb21186861'
    url = f'https://api.themoviedb.org/3/trending/movie/week?api_key={api_key}'
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({'error': 'Error connecting to the API'})

    data = response.json()
    results = data.get('results')

    if not results:
        return JsonResponse({'error': 'No movies found'})

    top_results = results[:10]
    movies = []

    for result in top_results:
        movie_title = result.get('original_title')
        poster_path = result.get('poster_path')

        if not movie_title or not poster_path:
            continue

        poster_url = f"https://image.tmdb.org/t/p/original/{poster_path}"
        movies.append({
            'title': movie_title,
            'poster_url': poster_url
        })

    return JsonResponse({'movies': movies})



@csrf_exempt
def search(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    query = request.POST.get('query')
    if not query:
        return JsonResponse({'error': 'No search query provided'})
    
    api_key = '6e65f8bcc3b3ca0c03e49fbb21186861'
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
    response = requests.get(url)
    if response.status_code != 200:
        return JsonResponse({'error': 'Error connecting to the API'})
    
    data = response.json()  
    results = data.get('results')
    if not results:
        return JsonResponse({'error': 'No movies found'})
    
    # Sort the movies by popularity in descending order
    sorted_results = sorted(results, key=lambda x: x.get('popularity', 0), reverse=True)
    top_results = sorted_results[:3]
    
    movies = []
    for result in top_results:
        movie_title = result.get('original_title')
        if not movie_title:
            continue
        
        poster_path = result.get('poster_path')
        if not poster_path:
            continue
        
        poster_url = f"https://image.tmdb.org/t/p/w185/{poster_path}"
        movies.append({
            'title': movie_title,
            'poster_url': poster_url
        })
    
    return JsonResponse({'movies': movies})
