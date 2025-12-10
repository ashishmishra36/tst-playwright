import json
import pytest
from playwright.sync_api import sync_playwright
from utils.logger import get_logger


log = get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption("--app-browser", action="store", default="chromium", choices=["firefox", "chromium"])

@pytest.fixture()
def page(request):
    browser_name = request.config.getoption("--app-browser")
    with sync_playwright() as p:
        log.info(f"Launching {browser_name} browser")
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page  # return the page object
        browser.close()


@pytest.fixture()
def fetch_test_data():
    with open('ecart/test_data/credentials.json') as f:
        test_data = json.load(f)
        # self.log.info('test data has been fetched')
        return test_data['user_credentials']
