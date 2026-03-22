from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure

from elements.input import Input


class LoginFromComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email') #page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        self.password_input = Input(page, 'login-form-password-input', 'Password')#page.locator('//div[@data-testid="login-form-password-input"]//div//input')

    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step("Check visible login form")
    def check_visible(self, email: str, password: str):
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)
        #expect(self.email_input).to_have_value(email)
        #expect(self.password_input).to_have_value(password)
