from behave import *  # noqa
from django.conf import settings

from movierama.users.factories import UserFactory, DUMMY_PASSWORD


@given(u'a user is on the Registration page')
def step_impl(context):
    context.browser.visit(context.get_url("account_signup"))
    assert context.browser.title == "Signup"
    assert context.browser.url == context.get_url("account_signup")


@when(u'fills the form')
def step_impl(context):
    for row in context.table:
        context.browser.fill(row['field'], row['value'])


@when(u'he press "{button}"')
def step_impl(context, button):
    context.browser.find_by_name(button).first.click()


@then(u'a MovieRama account is created for "{username}"')
def step_impl(context, username):
    from movierama.users.models import User
    assert User.objects.filter(username=username).exists()


@then(u'user is redirected to "{page}"')
def step_impl(context, page):
    assert context.browser.url == context.get_url(page)


@when(u'user is on the Login page')
def step_impl(context):
    context.browser.visit(context.get_url("account_login"))
    assert context.browser.title == "Sign In"
    assert context.browser.url == context.get_url("account_login")


@when(u'user is on the Home page')
def step_impl(context):
    context.browser.visit(context.get_url("homepage"))
    assert context.browser.title == "MovieRama"
    assert context.browser.url == context.get_url("homepage")


@given(u'existing user')
def step_impl(context):
    context.user = UserFactory()


@given(u'user is authenticated')
def step_impl(context):
    from movierama.users.utils import create_session_cookie

    session_key = create_session_cookie(username=context.user.username, password=DUMMY_PASSWORD)
    # to set a cookie we need to first visit the domain.
    # 404 pages load the quickest
    context.browser.get(context.get_url("/404_no_such_url/"))
    context.browser.cookies.add(dict(
        name=settings.SESSION_COOKIE_NAME,
        value=session_key,
        path='/',
    ))

    context.browser.get(context.get_url("homepage"))
    assert context.browser.is_element_present_by_css("li#navAccount")


@then(u'user is authenticated')
def step_impl(context):
    assert len(context.browser.find_by_id("user_menu")) > 0


@then(u'user is logged out')
def step_impl(context):
    assert len(context.browser.find_by_id("sign-up-link")) > 0
