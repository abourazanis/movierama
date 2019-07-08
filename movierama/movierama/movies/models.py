from django.db import models
from django.conf import settings


class Movie(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        # capitalize first letter of each word
        return '{}'.format(self.title.title())




