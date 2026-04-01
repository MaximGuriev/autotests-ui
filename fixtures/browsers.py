import pytest
from playwright.sync_api import Page, Playwright
from config import settings
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
import allure
from tools.routes import AppRoute

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name)

    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page =context.new_page()

    # yield page  # Создаем новую страницу
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()

    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_page_component.fill(email=settings.test_user.email,
                                                       username=settings.test_user.username,
                                                       password=settings.test_user.password)
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,storage_state=settings.browser_state_file, test_name=request.node.name)

    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(storage_state='browser-state.json', record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()

    # yield page

    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()

    # allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
