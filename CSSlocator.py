from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #CSS-Selector -> ID -> #

    # emailTextbox = page.wait_for_selector("#email")
    # emailTextbox.fill("test@gmail.com")
    #
    # buttonLogin = page.wait_for_selector("#enterimg")
    # buttonLogin.click()


    #CSS-Selector -> attributes -> tagname[attribute = "value"]

    username = page.wait_for_selector('input[name="username"]')
    username.fill('Admin')
    password = page.wait_for_selector('input[name="password"]')
    password.fill('admin123')
    loginbutton = page.wait_for_selector('button[type="submit"]')
    loginbutton.click()





