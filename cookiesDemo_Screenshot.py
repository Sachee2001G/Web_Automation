from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()


    page.goto('https://www.redbus.in')

    # Store cookies from website and deliver
    my_cookies = page.context.cookies()
    print(my_cookies)

    # clear cookies ->  erase the old cookies
    page.context.clear_cookies()

    # Insert some cookies

    new_cookies = {
        'name': 'shreya',
        'udid': '123456789'
    }

    # To pass the new cookies to the page.
    page.context.add_cookies(new_cookies)

    # Taking screenshot
    page.screenshot(path='test.png')

    # Taking screenshot fullscreen
    page.screenshot(path='test.png', full_page=True)
