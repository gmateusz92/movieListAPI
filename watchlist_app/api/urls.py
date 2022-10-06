from watchlist_app.api.views import MovieListAV, MovieDetailAV
from django.urls import path

urlpatterns = [
    #path('', views.movie_list, name='movie_list'),
    #path('<int:pk>/', views.movie_details, name='movie_detail'),
    path('', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_detail'),

]