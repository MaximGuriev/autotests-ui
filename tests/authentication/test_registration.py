from fixtures.pages import registration_page, dashboard_page
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

import pytest


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @pytest.mark.parametrize('email, username, password', [("user.name@gmail.com", "username", "password")])
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage, email: str,
                                     username: str, password: str):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_page_component.fill(email=email, username=username, password=password)
        registration_page.registration_page_component.check_visible(email=email, username=username, password=password)
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible_dashboard_title()
        # dashboard_page.students_chart_view.check_visible()
        # dashboard_page.activities_chart_view.check_visible()
        # dashboard_page.courses_chart_view.check_visible()
        # dashboard_page.scores_chart_view.check_visible()