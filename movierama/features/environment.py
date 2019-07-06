from selenium import webdriver
from splinter import Browser


def before_all(context):
    executable_path = {'executable_path': '/usr/bin/chromedriver'}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    context.browser = Browser('chrome', headless=True, options=chrome_options, **executable_path)

    context.server_url = 'http://localhost:8000/'


def after_all(context):
    # Explicitly quits the browser, otherwise it won't once tests are done
    context.browser.quit()


def before_feature(context, feature):
    # Code to be executed each time a feature is going to be tested
    pass
