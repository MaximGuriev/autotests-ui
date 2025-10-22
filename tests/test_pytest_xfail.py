import pytest


@pytest.mark.xfail(reason="Найден баг в приложение, из-за которого тест не проходит")
def test_with_bug():
    assert 1==2

@pytest.mark.xfail(reason="Баг уже не существует")
def test_without_bug():
    assert 1==1