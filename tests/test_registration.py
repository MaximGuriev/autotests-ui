from playwright.sync_api import sync_playwright, Page, expect

from fixtures.pages import registration_page, dashboard_page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


import pytest

@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('email, username, password', [("user.name@gmail.com", "username", "password")])
def test_successful_registration(dashboard_page: DashboardPage,registration_page: RegistrationPage, email: str, username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
    dashboard_page.check_visible_students_chart()
    dashboard_page.check_visible_activities_chart()
    dashboard_page.check_visible_courses_chart()
    dashboard_page.check_visible_scores_chart()


    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # context = chromium_page.new_context()
    #
    # email_input = chromium_page.get_by_test_id("registration-form-email-input").locator("input")
    # email_input.fill('user.me@gmail.com')
    #
    # username_input = chromium_page.get_by_test_id("registration-form-username-input").locator("input")
    # username_input.fill('username')
    #
    # password_input = chromium_page.get_by_test_id("registration-form-password-input").locator("input")
    # password_input.fill('password')
    #
    # registration_button = chromium_page.get_by_test_id("registration-page-registration-button")
    # registration_button.click()
    #
    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
    #
    # context.storage_state(path="browser-state-registration.json")
#
#       page.wait_for_timeout(500)
#
#    with sync_playwright() as playwright:
#        browser = playwright.chromium.launch(headless=False)
#        context = browser.new_context(storage_state='browser-state.json')
#
#       page = context.new_page()
#        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

#        page.wait_for_timeout(3000)