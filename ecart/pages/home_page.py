from pages.base_page import BasePage
from utils.logger import get_logger


class HomePage(BasePage):

    # Locators
    LOGIN_LINK = "a[href='/login']"
    LOGIN_HEADING = "//h2[text()='Login to your account']"

    def __init__(self, page):
        super().__init__(page)
        self.log = get_logger(__name__)

    # ---------------------------
    # Actions
    # ---------------------------
    def navigate_to_home(self, url):
        self.log.info(f"Opening home page: {url}")
        self.go_to(url)

    def click_login_link(self):
        self.wait_for_visible(self.LOGIN_LINK)
        self.log.info("Clicking login link")
        self.click(self.LOGIN_LINK)

    # ---------------------------
    # Getters
    # ---------------------------
    def get_home_title(self):
        return self.get_title()

    def get_login_heading(self):
        return self.page.locator(self.LOGIN_HEADING)
