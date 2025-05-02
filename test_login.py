import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("valid_user", "valid_pass")
    assert login_page.success_message_displayed()
