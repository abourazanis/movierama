from django.contrib import admin
from movierama.movies.models import Movie, MovieVote


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieVote)
class MovieVoteAdmin(admin.ModelAdmin):
    pass

