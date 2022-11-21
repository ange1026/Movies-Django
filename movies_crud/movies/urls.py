from django.urls import path
from .views import  MovieDetailView, MoviesView

urlpatterns = [
    path('', MoviesView.as_view(), name = 'movies'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie')
]