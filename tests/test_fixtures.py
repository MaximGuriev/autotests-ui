import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sending analytics data...")

@pytest.fixture(scope="session")
def settings():
    print("[SESSIOM] Loading settings...")

@pytest.fixture(scope="class")
def users():
    print("[CLASS] Loading users...")

@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Opening browser...")


class TestUserFlow:
    def test_user_can_login(self, settings, users, browser):
        ...

    def test_user_can_create_course(self, settings, users, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, users, browser):
        ...