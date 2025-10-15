import json

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def init_setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        # p.firefox.launch()
        # p.webkit.launch()

@pytest.fixture()
def fetch_test_data():
    with open('ecart/test_data/credentials.json') as f:
        test_data = json.load(f)
        print('test data has been fetched')
        return test_data['user_credentials']
