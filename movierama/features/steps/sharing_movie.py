from behave import *  # noqa

from movierama.movies.factories import MovieFactory


@then(u'a new Movie is added')
def step_impl(context):
    assert context.browser.is_text_present('successfully added.')


@given(u'there is a set of Movies in the Database')
def step_impl(context):
    for row in context.table:
        MovieFactory(title=row["title"], description=row["description"], date_created=row["date_created"])


@given(u'user is on the Home page')
def step_impl(context):
    context.browser.visit(context.get_url("homepage"))
    assert context.browser.title == "MovieRama"
    assert context.browser.url == context.get_url("homepage")


@then(u'the page includes "{movie_title}"')
def step_impl(context, movie_title):
    assert context.browser.is_text_present(movie_title)
