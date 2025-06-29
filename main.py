import time

from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(50000)
    page.goto('https://coinmarketcap.com/')
    time.sleep(2)

    for _ in range(5):
        page.mouse.wheel(0,500)
        time.sleep(3)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)