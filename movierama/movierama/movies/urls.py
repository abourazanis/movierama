from django.urls import path

from .views import create_movie

app_name = "movies"
urlpatterns = [
    path('create/', create_movie, name="create"),
]
