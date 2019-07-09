import factory
import datetime

from movierama.users.factories import UserFactory
from .models import Movie


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


