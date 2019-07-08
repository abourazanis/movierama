import factory
from django.contrib.auth.hashers import make_password
from .models import  User


DUMMY_PASSWORD = "123asd456"


class UserFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard active user.
    """
    class Meta:
        model = User
        django_get_or_create = ('username',)

    first_name = 'Jaime'
    last_name = 'Lannister'
    username = factory.Faker('user_name')
    password = make_password(DUMMY_PASSWORD)
    is_active = True
