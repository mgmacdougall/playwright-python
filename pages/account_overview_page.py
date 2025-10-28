"""Simple Page Object for the Parabank Accounts Overview page."""
from playwright.sync_api import Page
from typing import List


class AccountOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        # Header and accounts table locators (robust selectors)
        self.header = page.locator("h1.title:has-text('Accounts Overview')")
        self.accounts_table = page.locator("table#accountTable, table.accounts")

    def title_text(self) -> str:
        return self.header.text_content().strip() if self.header.count() else ""

    def account_ids(self) -> List[str]:
        """Return a list of account id strings found on the accounts overview table.

        This looks for anchor links inside the account table which typically contain
        the account id value.
        """
        links = self.page.locator("table#accountTable a, table.accounts a")
        return [t.strip() for t in links.all_text_contents()]

    def open_account(self, account_id: str) -> None:
        """Click on an account link by visible text (account id).

        Args:
            account_id: visible account id text to click.
        """
        # Use a text-based locator to find the link for the given account id
        self.page.locator(f"table#accountTable a:has-text('{account_id}'), table.accounts a:has-text('{account_id}')").click()
