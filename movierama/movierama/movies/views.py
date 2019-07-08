from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from movierama.movies.forms import MovieForm


class MovieCreateView(CreateView):
    form_class = MovieForm
    template_name = "movie_create.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse("homepage")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        messages.add_message(self.request, messages.SUCCESS,
                             'Movie "{}" successfully added.'.format(self.object),
                             fail_silently=True)

        return HttpResponseRedirect(self.get_success_url())


create_movie = MovieCreateView.as_view()

