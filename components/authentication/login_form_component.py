from components.base_component import BaseComponent
from playwright.sync_api import Page, expect



class LoginFromComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        self.password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')


    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self, email: str, password: str):
        expect(self.email_input).to_have_value(email)
        expect(self.password_input).to_have_value(password)
