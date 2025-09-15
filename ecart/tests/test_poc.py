import time

from playwright.sync_api import Page




# Note: by default playwright will launch in headless mode
# It has global fixture as playwright provided by pytest-playwright package
# chromium will support chrome and Edge, can be passed as channel value
def test_playwright(playwright):
    browser = playwright.chromium.launch(channel = 'chrome', headless=False) # it will return a browser object
    # browser = playwright.firefox.launch(headless=False)  # it will return a browser object
    context = browser.new_context() # it will launch a new incognito window of the new browser
    page = context.new_page()
    page.goto("http://www.rahulshettyacademy.com/")


# default Chrome browser in headless mode will be launched
# Better way : to import the page fixture from the Page class from
def test_playwright_other(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    print(page.title())
    try:
        #label text should be referred as id of element or input tag should inside the label
        page.get_by_label('username').fill('rahulshettyacademy')
        page.get_by_label('word').fill('learning')
        page.get_by_role('combobox').select_option('teach')
        page.get_by_label('terms').click()
        time.sleep(2)
        page.get_by_role('button', name= 'Sign In').click()
        time.sleep(2)
    except Exception as err:
        print(f'Exception found : {err}')


def test_playwright_expr(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    print(page.title())
    try:
        # It will find element based on text present under label
        page.get_by_role('textbox', name = 'email@example.com').fill('test@test.com')
        page.get_by_role('textbox', name = 'enter your passsword').fill('test@12345')
        time.sleep(2)
    except Exception as err:
        print(f'Exception found : {err}')



