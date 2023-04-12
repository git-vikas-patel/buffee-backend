from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster_url = models.URLField()

    def __str__(self):
        return self.title
    



class MovieDetails(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    release_date = models.DateField()
    synopsis = models.TextField()
    genre = models.CharField(max_length=200)
    cast_and_crew = models.TextField()
    production_companies = models.CharField(max_length=200)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    runtime = models.PositiveIntegerField()
    cover_art_url = models.URLField()
    trailer_and_video = models.TextField()
    reviews_and_ratings = models.TextField()
    download_links_480p = models.URLField()
    download_links_720p = models.URLField()
    download_links_1080p = models.URLField()
    download_links_4k = models.URLField()

    def __str__(self):
     return self.title
    
    