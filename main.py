import time

from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(50000)
    page.goto('https://practice.expandtesting.com/login')

    # Username: practice
    # Password: SuperSecretPassword!

    username_xpath = '//*[@id="username"]'
    password_xpath = '//*[@id="password"]'
    login_xpath = '//*[@id="login"]/button'

    page.wait_for_selector(username_xpath, timeout=10000)
    page.locator(username_xpath).fill('practice')
    time.sleep(5)

    page.wait_for_selector(password_xpath, timeout=10000)
    page.locator(password_xpath).fill('SuperSecretPassword!')
    time.sleep(5)

    page.locator(login_xpath).click()
    time.sleep(5)

    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.text)


    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)