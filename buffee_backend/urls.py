
from django.contrib import admin
from django.urls import path
from buffee import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.trending_movies, name='home'),
    path('search/', views.search, name='search_movies'),

]
