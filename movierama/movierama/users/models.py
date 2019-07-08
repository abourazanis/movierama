from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        # capitalize first letter of each word
        return '{}'.format(self.get_full_name().title())
