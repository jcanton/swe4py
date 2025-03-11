import pytest


def test_smoke():
    # a smoke test is typically used to verify that the application starts up without crashing
    assert True

def test_driver_username(monkeypatch):
    from project.app import Driver
    #monkeypatch.setenv('USERNAME', 'test_user')
    import os
    os.environ['USERNAME'] = 'test_user'
    driver = Driver('test_db')
    assert driver.username == 'test_user'
