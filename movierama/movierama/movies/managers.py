from collections import defaultdict

from django.db import models, transaction
from django.db.models import QuerySet, Count, Case, IntegerField, When
from django.apps import apps


class VotedMovieQuerySet(QuerySet):

    def annotate_votes(self):
        return (
            self.annotate(
                likes_count=Count(
                    Case(
                        When(votes__vote=True, then=1),
                        output_field=IntegerField(),
                    )
                ),
                hates_count=Count(
                    Case(
                        When(votes__vote=False, then=1),
                        output_field=IntegerField(),
                    )
                )
            )
        )

    def order_by_likes(self):
        return (
            self.order_by("-likes_count", "-date_created")
        )

    def order_by_hates(self):
        return (
            self.order_by("-hates_count", "-date_created")
        )


class MoviesManager(models.Manager):

    def __init__(self, user_id=None, *args, **kwargs):
        self.user_id = user_id
        super().__init__(*args, **kwargs)

    @classmethod
    def factory(cls, model, user_id=None):
        manager = cls(user_id)
        manager.model = model
        return manager

    def get_queryset(self) -> VotedMovieQuerySet:
        queryset = VotedMovieQuerySet(
            model=self.model,
            using=self._db,
            hints=self._hints)

        queryset = queryset.annotate_votes()

        if self.user_id is not None:
            queryset = self.vote_annotated(queryset, self.user_id)

        return queryset

    def vote_annotated(self, queryset, user_id):
        """
        In case that 'user' has voted (or not) each movie instance,
        we add a voted attribute on each movie, with the following values
        'voted' = True, user has liked the movie
        'voted' = False, user has hated the movie
        'voted' = None, user has not voted the movie

        """

        voted_users = defaultdict()

        # In order to avoid circular imports
        MovieVote = apps.get_model('movies', 'MovieVote')

        votes = MovieVote.objects.filter(movie_id__in=queryset.values_list('id'))

        # add each user that has voted in a dict with key the movie id
        # so we will have a dict of dicts with the following format:
        # { movie_id: { user_id: vote}}
        for v in votes:
            if v.movie_id in voted_users.keys():
                voted_users[v.movie_id].update({v.user_id: v.vote})
            else:
                voted_users[v.movie_id] = {v.user_id: v.vote}

        for r in queryset:
            votes = voted_users.get(r.id, {})
            r.voted = votes[user_id] if user_id in votes.keys() else None

        return queryset

    def order_by_likes(self):
        queryset = self.get_queryset()
        return queryset.order_by_likes()

    def order_by_hates(self):
        queryset = self.get_queryset()
        return queryset.order_by_hates()
