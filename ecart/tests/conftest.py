import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def init_setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        # p.firefox.launch()
        # p.webkit.launch()
