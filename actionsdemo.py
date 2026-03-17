from playwright.sync_api import sync_playwright
text_alert = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Alerts.html')


    # MOUSE ACTIONS

    # To hover over dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()

    #To click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()

    # To double-click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()

    # To right-click on element
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')


    # shift click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])


    # KEY-BOARD ACTIONS

    # A-Z,0-9, F1-F12, All special character, ArrowRight, ArrowDown,Pageup,Enter,Control, Comand

    page.wait_for_selector('//a[text()="SwitchTo"]').press("A")

    page.wait_for_selector('//a[text()="SwitchTo"]').press("$")

    page.wait_for_timeout(2000)