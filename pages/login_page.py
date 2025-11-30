from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from playwright_hover import registration_link


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        self.password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        self.login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')


    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_regisration_lonk(self):
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_have_text('Wrong email or password')
