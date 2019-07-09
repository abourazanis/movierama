from django.db import models, transaction
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from movierama.movies.managers import MoviesManager


def factory_manager_for_user(user_id):
    return MoviesManager.factory(model=Movie, user_id=user_id)


class Movie(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = MoviesManager()
    as_user = factory_manager_for_user

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        # capitalize first letter of each word
        return '{}'.format(self.title.title())

    def vote(self, user, vote):
        # A user cannot vote his own movie
        if self.user_id == user.id:
            # TODO: raise an error that can be consumed in front
            return None

        with transaction.atomic():
            movievote, created = self.votes.get_or_create(user=user, movie=self)
            movievote.vote = vote
            movievote.save()

    def like(self, user):
        return self.vote(user, True)

    def hate(self, user):
        return self.vote(user, False)

    def remove_vote(self, user):
        try:
            self.votes.get(user=user, movie=self).delete()
        except Exception as e:
            pass

    def vote_exists(self, user):
        return self.votes.filter(user=user).exists()

    def likes(self):
        return self.votes.filter(vote=True).count()

    def hates(self):
        return self.votes.filter(vote=False).count()

    def voted_users(self):
        return self.votes.values_list('user_id')


class MovieVote(models.Model):
    CHOICES = (
        (True, _('like')),
        (False, _('hate')),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes', on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', related_name='votes', on_delete=models.CASCADE)
    vote = models.BooleanField(choices=CHOICES, default=True)

    class Meta:
        unique_together = (
            ('user', 'movie'),
        )

    def __str__(self):
        return '{} {}s {}'.format(self.user, self.get_vote_display(), self.movie)
