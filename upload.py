
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practice.expandtesting.com/upload")
    page.get_by_test_id("file-input").set_input_files(r"D:\scraping\playwright\pw-bs4\1751246758151_test_file.txt")
    page.get_by_test_id("file-submit").click()
    time.sleep(10)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
