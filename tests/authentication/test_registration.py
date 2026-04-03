from fixtures.pages import registration_page, dashboard_page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag

from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from allure_commons.types import Severity
from tools.routes import AppRoute

import pytest
import allure


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGISTRATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @pytest.mark.parametrize('email, username, password', [("user.name@gmail.com", "username", "password")])
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage, email: str,
                                     username: str, password: str):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_page_component.fill(email=email, username=username, password=password)
        registration_page.registration_page_component.check_visible(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible_dashboard_title()
        # dashboard_page.students_chart_view.check_visible()
        # dashboard_page.activities_chart_view.check_visible()
        # dashboard_page.courses_chart_view.check_visible()
        # dashboard_page.scores_chart_view.check_visible()