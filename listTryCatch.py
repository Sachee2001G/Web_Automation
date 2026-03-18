from playwright.sync_api import sync_playwright
text_alert = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Selectable.html')

    # Store multiple elements using list

    # elements = page.query_selector_all('b')
    # print(len(elements))
    # for i in elements:
    #     print(i.text_content())
    # page.wait_for_timeout(5000)

    # For anchor tag

    elements = page.query_selector_all('a')
    print(len(elements))
    for i in elements:
        print(i.get_attribute('href'))
    page.wait_for_timeout(5000)
