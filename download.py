import os
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        accept_downloads=True,
        viewport={'width': 1280, 'height': 1024}
    )

    page = context.new_page()

    try:
        # Navigate to the page
        page.goto("https://practice.expandtesting.com/download", timeout=60000)
        page.wait_for_load_state('networkidle')

        # Get the first download link (or specify which one you want)
        # Option 1: Get first download link
        # download_link = page.locator('a[download][href*="test_file.txt"]').first

        # Option 2: Get by exact testid if you know it (replace with current testid)
        download_link = page.get_by_test_id("1751246758151_test_file.txt")

        # Option 3: Get by visible text if you have specific text
        # download_link = page.get_by_text("Download test_file.txt", exact=True)

        # Wait for and click the specific download link
        download_link.wait_for(timeout=60000)

        with page.expect_download(timeout=60000) as download_info:
            download_link.click()

        download = download_info.value

        # Define download path
        download_path = r'D:\scraping\playwright\pw-bs4'
        os.makedirs(download_path, exist_ok=True)

        # Save file
        download_file_path = os.path.join(download_path, download.suggested_filename)
        download.save_as(download_file_path)
        print(f'File successfully saved to: {download_file_path}')

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        page.screenshot(path='error_screenshot.png')
        print("Screenshot saved to error_screenshot.png")
    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)