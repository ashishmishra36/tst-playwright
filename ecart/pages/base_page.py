from playwright.sync_api import Page, Locator
from utils.logger import get_logger


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        # gets the name of the class (here, "BasePage" or the child class name when inherited).
        self.log = get_logger(self.__class__.__name__)

    # ---------------------------
    # Navigation
    # ---------------------------
    def go_to(self, url: str):
        self.log.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    # ---------------------------
    # Click wrapper
    # ---------------------------
    def click(self, locator: str | Locator):
        self.log.info(f"Clicking on: {locator}")
        self.page.locator(locator).click()

    # ---------------------------
    # Type wrapper
    # ---------------------------
    def type(self, locator: str, value: str, clear=True):
        if clear:
            self.log.info(f"Clearing + typing '{value}' into: {locator}")
            self.page.locator(locator).fill(value)
        else:
            self.log.info(f"Typing '{value}' into: {locator}")
            self.page.locator(locator).type(value)

    # ---------------------------
    # Read text
    # ---------------------------
    def get_text(self, locator: str) -> str:
        self.log.info(f"Getting text from: {locator}")
        return self.page.locator(locator).text_content()

    # ---------------------------
    # Waits
    # ---------------------------
    def wait_for_visible(self, locator: str | Locator):
        self.log.info(f"Waiting for: {locator} to be visible")
        return self.page.locator(locator).wait_for(state="visible")

    def wait_for_clickable(self, locator: str):
        self.log.info(f"Waiting for element to be clickable: {locator}")
        self.page.locator(locator).wait_for(state="visible")

    # ---------------------------
    # Page Title
    # ---------------------------
    def get_title(self):
        title = self.page.title()
        self.log.info(f"Current page title: {title}")
        return title
