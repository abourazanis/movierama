from behave import *  # noqa

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
    context.browser.find_by_id(button).first.click()


@when(u'he press on the "{link}" link')
def step_impl(context, link):
    # splinter bug in links interactions
    # context.browser.click_link_by_id(link)
    # use direct url call instead
    context.browser.visit(context.get_url("account_logout"))


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
    assert context.browser.title == "Log In"
    assert context.browser.url == context.get_url("account_login")


@when(u'user is on the Home page')
def step_impl(context):
    context.browser.visit(context.get_url("homepage"))
    assert context.browser.title == "MovieRama"
    assert context.browser.url == context.get_url("homepage")


@given(u'existing user')
def step_impl(context):
    context.user = UserFactory(username="jaimelan")


@given(u'user is authenticated')
def step_impl(context):
    context.browser.visit(context.get_url("account_login"))
    context.browser.fill("login", context.user.username)
    context.browser.fill("password", DUMMY_PASSWORD)
    context.browser.find_by_id("btn_login").first.click()

    assert context.browser.find_by_id("user_menu").first


@then(u'user is authenticated')
def step_impl(context):
    assert context.browser.find_by_id("user_menu").first


@then(u'user is logged out')
def step_impl(context):
    context.browser.visit(context.get_url("homepage"))
    assert context.browser.find_by_id("log_in_link").first
