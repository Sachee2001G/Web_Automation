# AJAX ->
# web development technique that allows web pages to send and receive data from a server in the background, without reloading the entire page.

from playwright.sync_api import sync_playwright



def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php?' in response.url:
        status = response.status
        data = response.text()
        print(f'status:{status},data:{data}')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')

    select = page.wait_for_selector('//select[@id="s1"]')
    page.on('response', lambda response: handle_rejex(response))

    select.select_option('1')

    page.wait_for_timeout(2000)