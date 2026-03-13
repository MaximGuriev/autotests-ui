import re

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from typing import Pattern

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_page_component = RegistrationFormComponent(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login')

        self.password_input = Input(page, 'registration-form-password-input', 'Password')#page.get_by_test_id("registration-form-password-input").locator("input")
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration button')#page.get_by_test_id("registration-page-registration-button")
        self.dashboard_title = Text(page, 'dashboard-toolbar-title-text', 'Title')#page.get_by_test_id('dashboard-toolbar-title-text')



    def click_registration_button(self):
        self.registration_button.click()


    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))
