import pytest
from playwright.sync_api import  Page, Playwright, expect

pytest.mark.usefixtures('initialize_browser_state')
def test_empty_courses_list(chromium_page_with_state) -> Page:

    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_be_visible()
    expect(courses).to_contain_text("Courses")

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title).to_be_visible()
    expect(title).to_contain_text("There is no results")

    description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description).to_be_visible()
    expect(description).to_contain_text("Results from the load test pipeline will be displayed here")



