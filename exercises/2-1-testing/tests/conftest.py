import pytest

@pytest.fixture
def set_env_vars(monkeypatch):
    """Fixture to set environment variables for testing."""
    monkeypatch.setenv('USERNAME', 'test_user')
    monkeypatch.setenv('PASSWORD', 'test_password')
