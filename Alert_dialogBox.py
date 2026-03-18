from playwright.sync_api import sync_playwright
text_alert = []

#Make a function
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    # From parent div
    # page.wait_for_selector('//div[@id="OKTab"]/button').click()


    # control alert
    # page.on("dialog",lambda dialog : dialog.accept())

    #print the message of the dialog box
    # page.on("dialog", lambda dialog : print(dialog.message))



    # If you want to check on cancel button:
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()




    page.wait_for_timeout(2000)