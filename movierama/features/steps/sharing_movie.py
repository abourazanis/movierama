from behave import *  # noqa

from movierama.movies.factories import MovieFactory, MovieVoteFactory
from movierama.users.factories import UserFactory


@then(u'a new Movie is added')
def step_impl(context):
    assert context.browser.is_text_present('successfully added.')


@given(u'there is a set of Movies in the Database')
def step_impl(context):
    for row in context.table:
        user = UserFactory(username=row["username"])
        movie = MovieFactory(title=row["title"], description=row["description"], date_created=row["date_created"], user=user)
        for i in range(0, int(row["hates"])):
            MovieVoteFactory(movie=movie, vote=False)
        for i in range(0, int(row["likes"])):
            MovieVoteFactory(movie=movie, vote=True)


@given(u'user is on the Home page')
def step_impl(context):
    context.browser.visit(context.get_url("homepage"))
    assert context.browser.title == "MovieRama"
    assert context.browser.url == context.get_url("homepage")


@then(u'the page includes "{movie_title}"')
def step_impl(context, movie_title):
    assert context.browser.is_text_present(movie_title)


@when(u'he clicks on the name of user "{username}"')
def step_impl(context, username):
    # splinter bug in links interactions
    # context.browser.click_link_by_id(username)
    # use direct url call instead
    context.browser.visit(context.get_url('userpage', username=username))


@then(u'movie with title "{movie}" should be first')
def step_impl(context, movie):
    element = context.browser.find_by_css('h3').first
    print(element.value)
    assert context.browser.find_by_css('h3').first.value == movie


@given(u'existing movie "{movie}" of user "{username}"')
def step_impl(context, movie, username):
    user = UserFactory(username=username)
    context.movie = MovieFactory(title=movie, user=user)


@when(u'user likes Movie')
def step_impl(context):
    context.old_likes = context.movie.likes()
    context.movie.like(context.user)


@then(u'the number of likes of the movie is increased by "{count:d}"')
def step_impl(context, count):
    assert context.old_likes + count == context.movie.likes()


@when(u'user hates Movie')
def step_impl(context):
    context.old_hates = context.movie.hates()
    context.movie.hate(context.user)


@then(u'the number of hates of the movie is increased by "{count:d}"')
def step_impl(context, count):
    assert context.old_hates + count == context.movie.hates()


@then(u'a movievote for "{user}" and "{movie}" is not created')
def step_impl(context, user, movie):
    from movierama.movies.models import MovieVote
    assert MovieVote.objects.filter(movie__title=movie, user__username=user).exists() is False


@then(u'a new Movie with title "{title}" is not added')
def step_impl(context, title):
    from movierama.movies.models import Movie
    assert Movie.objects.filter(title=title).count() == 1


@given(u'user likes Movie')
def step_impl(context):
    context.movie.like(context.user)
    context.old_likes = context.movie.likes()


@when(u'user removes vote')
def step_impl(context):
    context.movie.remove_vote(context.user)


@then(u'the number of likes of the movie is descreased by "{count:d}"')
def step_impl(context, count):
    assert context.old_likes - count == context.movie.likes()

