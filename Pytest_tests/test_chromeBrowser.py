import pytest
from playwright.sync_api import Playwright

# Creating a method

def test_login(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == 'OrangeHRM'