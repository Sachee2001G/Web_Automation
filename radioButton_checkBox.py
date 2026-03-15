from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # Radio Button
    radio_button = page.query_selector('//input[@value="FeMale"]')

    # Click and Check
    # radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
        print('Passed !')
    else:
        print('Failed !')


    # Check-Box
    checkbox = page.query_selector('//input[@value="Cricket"]')
    checkbox.click()
    if checkbox.is_checked():
        print('Passed !')
    else:
        print('Failed !')


    page.wait_for_timeout(3000)