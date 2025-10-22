from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
              wait_until="networkidle")

    # unknon = page.locator('#unknown')
    # expect(unknon).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('nikita')

    next_text = 'Another Text'
    page.evaluate(f"""
     const title = document.getElementById('authentication-ui-course-title-text');
     title.textContent = '{next_text}';
     """)