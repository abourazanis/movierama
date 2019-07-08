from behave import *  # noqa


@then(u'a new Movie is added')
def step_impl(context):
    assert context.browser.is_text_present('successfully added.')
