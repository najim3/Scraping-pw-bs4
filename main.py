# from playwright.async_api import Playwright
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright, expect



def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://quotes.toscrape.com/js/')

    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')

    text = soup.find('span', class_='text')
    print(text.text)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)