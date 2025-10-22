import pytest

SYSTEM_VERSION = "v1.2.3"

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.0",
    reason = "Тест не может быть запущен на  версии системы v1.3.0"
)
def test_system_version_valid():
    ...

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.2.3",
    reason = "Тест не может быть запущен на  версии системы v1.2.3"
)
def test_system_version_invalid():
    ...