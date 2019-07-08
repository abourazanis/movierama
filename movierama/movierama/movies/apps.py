from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MoviesConfig(AppConfig):
    name = "movierama.movies"
    verbose_name = _("Movies")

    def ready(self):
        try:
            import movierama.movies.signals  # noqa F401
        except ImportError:
            pass
