from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #Xpath - Relative xpath '//'
    #Using attribute -> //tagname[@attributename="value"]

    username_element = page.wait_for_selector('//input[@name="username"]')
    username_element.fill('Admin')
    password_element = page.wait_for_selector('//input[@placeholder="password"]')
    password_element.fill('admin123')
    login_element = page.wait_for_selector('//button[@type="submit"]')
    login_element.click()
    page.wait_for_timeout(3000)

    # Text Method -> tagname[text()='text']

    page.wait_for_selector('//p[text()="Forgot your password?"]')

    # contains
    # attributes -> //tagname[contains(@attributes,"value")]
    # text -> //tagname
    # //label[contains(text(), "Username")]
    # dynamic - sachee123, sachee12345, sachee154
    # starts-with -> //tagname[starts-with(@id,'sachee')]
    # ends-with -> 246

    # family

    #parent -> //tagname[@id = "XY"]/parent::input[]
    #child -> //tagname[@id = "XY"]/child::input[]
    #ancestor