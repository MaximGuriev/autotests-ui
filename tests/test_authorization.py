from playwright.sync_api import sync_playwright, expect, Page # Импорт Playwright для синхронного режима и проверки

from components.authentication.login_form_component import LoginFromComponent
from pages.login_page import LoginPage

import pytest

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', [("user.name@gmail.com", "password"),
                                             ("user.name@gmail.com", "  " ),
                                             ("  " , "password")])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str, login_form: LoginFromComponent):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_form.fill(email=email, password=password)
    login_form.check_visible(email=email, password=password)

    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

