from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')#page.get_by_test_id("registration-form-email-input").locator("input")
        self.username_input = Input(page, 'registration-form-username-input', 'Username')#page.get_by_test_id("registration-form-username-input").locator("input")
        self.password_input = Input(page, 'registration-form-password-input', 'Password')#page.get_by_test_id("registration-form-password-input").locator("input")


    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)


    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)

