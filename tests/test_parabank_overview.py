"""Test suite for Parabank account overview functionality."""
import os
import re
import pytest
from playwright.sync_api import Page, expect
from pages.parabank_login_page import ParabankLoginPage
from pages.account_overview_page import AccountOverviewPage


@pytest.fixture
def logged_in_page(page: Page, base_url: str) -> Page:
    """Fixture that logs in to Parabank and returns the page object.
    
    Requires PARABANK_USERNAME and PARABANK_PASSWORD environment variables.
    """
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)
    
    username = os.getenv("PARABANK_USERNAME", "john")
    password = os.getenv("PARABANK_PASSWORD", "demo")
    
    login_page.login(username, password)
    return page


def test_account_overview_after_login(logged_in_page: Page):
    """Test that account overview page loads after login with correct elements."""
    overview = AccountOverviewPage(logged_in_page)
    
    # Header should be visible and contain expected text
    expect(overview.header).to_be_visible()
    expect(overview.header).to_contain_text("Accounts Overview")
    
    # Account table should be present
    expect(overview.accounts_table).to_be_visible()


def test_account_list_not_empty(logged_in_page: Page):
    """Test that the account overview shows at least one account."""
    overview = AccountOverviewPage(logged_in_page)
    account_ids = overview.account_ids()
    
    assert len(account_ids) > 0, "Expected at least one account to be listed"
    # First account ID should be a non-empty string
    assert account_ids[0].strip(), "Account ID should not be empty"


def test_can_click_account_details(logged_in_page: Page):
    """Test that clicking an account ID navigates to account details."""
    overview = AccountOverviewPage(logged_in_page)
    account_ids = overview.account_ids()
    
    if not account_ids:
        pytest.skip("No accounts available to test")
    
    # Click the first account
    overview.open_account(account_ids[0])
    
    # Should be on account details page
    expect(logged_in_page).to_have_url(re.compile(r".*activity.htm.*"))
    # Account details should show the account ID we clicked
    account_details = logged_in_page.locator("#accountId")
    expect(account_details).to_contain_text(account_ids[0])


@pytest.mark.parametrize("section", [
    "Open New Account",
    "Transfer Funds",
    "Bill Pay",
    "Find Transactions"
])
def test_account_services_links(logged_in_page: Page, section: str):
    """Test that account service links are visible and clickable."""
    # Links are in a list with class="leftmenu"
    link = logged_in_page.locator(f".leftmenu a:has-text('{section}')")
    expect(link).to_be_visible()
    
    # Click should work without errors
    link.click()
    # URL should reflect the section
    expect(logged_in_page.url).to_contain(section.lower().replace(" ", ""))


@pytest.mark.skip(reason="Add this when account creation is implemented")
def test_new_account_appears_in_overview(logged_in_page: Page):
    """Test that a newly created account appears in the overview list.
    
    This test requires implementation of account creation functionality.
    """
    # TODO: Implement after adding account creation page object
    pass