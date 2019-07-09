from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin

from movierama.movies.forms import MovieForm
from movierama.movies.models import Movie


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


class MovieListView(ListView):
    model = Movie
    template_name = "pages/home.html"
    context_object_name = "movies"

    def get_ordering(self):
        order_by_mapping = {"date": "-date_created", "likes": "", "hates": ""}
        order_by = self.request.GET.get('order_by', None)

        if order_by and order_by in order_by_mapping.keys():
            self.ordering = order_by_mapping[order_by]

        return self.ordering

    def get_queryset(self):
        queryset = super().get_queryset()

        filter = self.kwargs.get("username", None)
        if filter:
            queryset = queryset.filter(user__username=filter)

        return queryset


movieslist = MovieListView.as_view()

