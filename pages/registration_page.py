from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page, expect



class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_page_component = RegistrationFormComponent(page)

        self.password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        self.registration_button = page.get_by_test_id("registration-page-registration-button")
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')



    def click_registration_button(self):
        self.registration_button.click()
