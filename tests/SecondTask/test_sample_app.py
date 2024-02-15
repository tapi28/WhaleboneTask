# Description: This file contains the test cases for the Sample App page.
import pytest


def test_sample_app_is_loaded(sample_app_page):
    assert sample_app_page.is_sample_app_loaded()


@pytest.mark.parametrize(
    "username, password",
    [("admin", "pwd"), ("123", "pwd"), ("Ad@?1", "pwd")],
)
def test_login_is_successful(sample_app_page, username, password):
    sample_app_page.login(username=username, password=password)
    assert sample_app_page.login_successful.is_visible()
    assert sample_app_page.logout_button.is_visible()


@pytest.mark.parametrize(
    "username, password",
    [("admin", "admin"), ("", "pwd"), ("admin", "")],
)
def test_login_is_not_successful(sample_app_page, username, password):
    sample_app_page.login(username="username", password="password")
    assert sample_app_page.login_failed.is_visible()


def test_logout_is_successful(sample_app_page):
    sample_app_page.login(username="admin", password="pwd")
    sample_app_page.logout()
    assert sample_app_page.logout_successful.is_visible()
