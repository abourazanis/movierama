from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin, FormView, ProcessFormView

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
        return self.request.GET.get('order_by', None)

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.user.is_authenticated:
            queryset = self.model.as_user(self.request.user.id).all()

        username = self.kwargs.get("username", None)
        if username:
            queryset = queryset.filter(user__username=username)

        ordering = self.get_ordering()
        if ordering:
            if ordering == "date":
                queryset = queryset.order_by("-date_created")
            if ordering == "likes":
                queryset = queryset.order_by_likes()
            if ordering == "hates":
                queryset = queryset.order_by_hates()

        return queryset


movieslist = MovieListView.as_view()


class VoteMovieView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=kwargs.get('movie_id', None))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse("homepage"))

        vote = request.POST.get('vote', None)
        if vote is not None:
            movie.vote(self.request.user, vote)

        return HttpResponseRedirect(reverse("homepage"))


vote_movie = VoteMovieView.as_view()


class UnVoteMovieView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=kwargs.get('movie_id', None))
        except ObjectDoesNotExist as e:
            return HttpResponseRedirect(reverse("homepage"))

        movie.remove_vote(self.request.user)

        return HttpResponseRedirect(reverse("homepage"))


unvote_movie = UnVoteMovieView.as_view()



