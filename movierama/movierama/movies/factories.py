import factory
import datetime

from factory.fuzzy import FuzzyChoice

from movierama.users.factories import UserFactory
from .models import Movie, MovieVote


class MovieFactory(factory.django.DjangoModelFactory):
    """
    Creates a Movie.
    """

    user = factory.SubFactory(UserFactory)
    title = factory.Faker('text', locale='en_US')
    description = factory.Faker('text', locale='en_US')
    date_created = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = Movie
        django_get_or_create = ('title', 'user')


class MovieVoteFactory(factory.django.DjangoModelFactory):
    """
    Creates a MovieVote
    """

    user = factory.SubFactory(UserFactory)
    movie = factory.SubFactory(MovieFactory)
    vote = FuzzyChoice(choices=MovieVote.CHOICES)

    class Meta:
        model = MovieVote
        django_get_or_create = ('user', 'movie')

