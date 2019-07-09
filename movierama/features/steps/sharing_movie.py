from behave import *  # noqa
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from movierama.movies.factories import MovieFactory
from movierama.users.factories import UserFactory


@then(u'a new Movie is added')
def step_impl(context):
    assert context.browser.is_text_present('successfully added.')


@given(u'there is a set of Movies in the Database')
def step_impl(context):
    for row in context.table:
        user = UserFactory(username=row["username"])
        MovieFactory(title=row["title"], description=row["description"], date_created=row["date_created"], user=user)


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
    assert context.browser.find_by_css('h3').first.value == movie

