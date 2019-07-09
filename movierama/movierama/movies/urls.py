from django.urls import path

from .views import create_movie, vote_movie, unvote_movie

app_name = "movies"
urlpatterns = [
    path("create/", create_movie, name="create"),
    path("<movie_id>/vote/", vote_movie, name="vote"),
    path("<movie_id>/unvote/", unvote_movie, name="unvote")

]
