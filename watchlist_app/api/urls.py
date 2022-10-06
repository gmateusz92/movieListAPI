from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV
from django.urls import path

urlpatterns = [
    #path('', views.movie_list, name='movie_list'),
    #path('<int:pk>/', views.movie_details, name='movie_detail'),
    path('list', WatchListAV.as_view(), name='movie_list'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform_detail'),

]