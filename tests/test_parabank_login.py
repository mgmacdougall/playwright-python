"""Test suite for Parabank login functionality using Page Object Model."""
import pytest
from playwright.sync_api import Page, expect
from pages.parabank_login_page import ParabankLoginPage
from pages.account_overview_page import AccountOverviewPage

def test_parabank_login_page_loads(page: Page, base_url: str):
    """Test that the Parabank login page loads and contains expected elements."""
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)
    
    # Check that login form elements are visible
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_parabank_invalid_login(page: Page, base_url: str):
    """Test login with invalid credentials shows an error."""
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)
    login_page.login("invalid_user", "invalid_pass")
    
    # Error message appears in a paragraph with class="error"
    error = page.locator("p.error")
    expect(error).to_be_visible()
    expect(error).to_contain_text("The username and password could not be verified.")


def test_parabank_valid_login(page: Page, base_url: str):
    """Test successful login with valid credentials.
    
    Note: Update credentials and remove skip marker to run this test.
    Consider using environment variables for credentials in CI/CD.
    """
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)
    
    # TODO: Use environment variables or vault for credentials
    login_page.login("john", "demo")
    
    # After login, we should see the accounts overview
    overview = AccountOverviewPage(page)
    expect(overview.header).to_be_visible()
    expect(overview.header).to_contain_text("Accounts Overview")
    
    # Should have at least one account visible
    account_ids = overview.account_ids()
    assert len(account_ids) > 0, "Expected at least one account after login"


@pytest.mark.parametrize("username,password,expected_error", [
    ("", "", "Please enter a username and password."),
    ("user123", "", "Please enter a username and password."),
    ("", "pass123", "Please enter a username and password."),
])
def test_parabank_login_validation(page: Page, base_url: str, username: str, password: str, expected_error: str):
    """Test login form validation for various invalid input combinations."""
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)
    login_page.login(username, password)
    
    # Error message should contain expected text
    error = page.locator("p.error")
    expect(error).to_be_visible()
    expect(error).to_contain_text(expected_error)