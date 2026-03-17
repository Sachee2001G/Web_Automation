from playwright.sync_api import sync_playwright
text_alert = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Alerts.html')

    page.wait_for_selector('//a[text()="SwitchTo"]').hover()

    page.wait_for_timeout(2000)