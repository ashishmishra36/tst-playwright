from tests.test_base import BaseTest
from pages.home_page import HomePage
from configs.config import TestData
from playwright.sync_api import expect
from utils.logger import get_logger


class TestHome(BaseTest):
    log = get_logger(__name__)

    def test_has_title(self, page):
        home = HomePage(page)

        home.navigate_to_home(TestData.BASE_URL)
        self.log.info(f"Page title: {home.get_home_title()}")
        expect(page).to_have_title("Automation Exercise")

    def test_get_started_link(self, page):
        home = HomePage(page)

        home.navigate_to_home(TestData.BASE_URL)
        home.click_login_link()
        self.log.info("Login link clicked")
        expect(home.get_login_heading()).to_be_visible()
