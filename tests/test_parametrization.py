import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    #print(f'Number: {number}')
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request):
    return request.param

def test_open_browser(browser:str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperation:
    @pytest.mark.parametrize('account', ['credit card', 'Debit card'])
    def test_user_with_operation(self, user: str, account: str):
        ...

    def test_user_without_operations(self, user: str):
        ...

users = {
    '8-8000-555-35-35': 'User with money on bank account',
    '8-8000-555-35-36': 'User without money on bank account',
    '8-8000-555-35-37': 'User with operation on bank account'
}
#Пример с функцией
def format_phone_number(phone_number: str) ->str:
    return f'{phone_number}: {users[phone_number]}'


@pytest.mark.parametrize('phone_number',
                         users.keys(),
                         ids = format_phone_number
                         #ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...


