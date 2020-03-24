from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie


class MoviesView(ListView):
    """List of movies"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movie_app/movies.html"


class MovieDetailView(DetailView):
    """Full desc movie"""
    model = Movie
    slug_field = "url"

