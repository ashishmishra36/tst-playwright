import time

from playwright.sync_api import Page, expect


fake_no_orders_response ={"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fake_no_orders_response)

def test_network(page:Page):
    page.goto('https://rahulshettyacademy.com/client')
    expect(page).to_have_title("Let's Shop")
    print(f'Page has title as {page.title()}')
    # intercept the call to get orders -> Simulate the fake response -> validate the rendered fake response
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', handler=intercept_response)
    # Login
    page.locator('#userEmail').fill('demo@playwright.com')
    page.locator('#userPassword').fill('Qwe@1234')
    page.get_by_role('button', name='login').click()
    time.sleep(5)
    #click on orders
    page.get_by_role('button', name='ORDERS').click()
    text= page.locator(".mt-4").text_content()

    print(f'text appears as :{text}' )
