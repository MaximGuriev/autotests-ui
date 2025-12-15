import pytest
from playwright.sync_api import Page, Playwright, expect

from fixtures.pages import CreateCoursePage, CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage) -> Page:
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disable_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_create_course_form('', '', '', '0', '0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()

    create_course_page.fill_create_course_form(title="Playwright", estimated_time="2 weeks", description="Playwright",
                                               max_score="100", min_score="10")
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_course_card(index=0, title="Playwright", max_score="100", min_score="10",
                                                estimated_time="2 weeks")
