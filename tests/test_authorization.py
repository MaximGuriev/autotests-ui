from playwright.sync_api import sync_playwright, expect, Page  # Импорт Playwright для синхронного режима и проверки
import pytest

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
# Переходим на страницу авторизации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим поле "Email" и заполняем его
    email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Password" и заполняем его
    password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее
    login_button = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    wrong_email_or_password_alert = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible()  # Проверяем видимость элемента
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")  # Проверяем текст

    # Пауза на 5 секунд, чтобы увидеть результат
    # page.wait_for_timeout(5000)