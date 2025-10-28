"""Page object for Parabank Transfer Funds page."""
from playwright.sync_api import Page


class TransferFundsPage:
    def __init__(self, page: Page):
        self.page = page
        self.amount_input = page.locator("input[name='amount']")
        self.from_account_select = page.locator("select[name='fromAccountId']")
        self.to_account_select = page.locator("select[name='toAccountId']")
        self.transfer_button = page.locator("input[value='Transfer'], button:has-text('Transfer')")

    def transfer(self, amount: float, from_account: str = None, to_account: str = None) -> None:
        """Perform a transfer between accounts.

        Args:
            amount: amount to transfer
            from_account: value attribute of the from account option (optional)
            to_account: value attribute of the to account option (optional)
        """
        self.amount_input.fill(str(amount))
        if from_account:
            self.from_account_select.select_option(value=str(from_account))
        if to_account:
            self.to_account_select.select_option(value=str(to_account))
        self.transfer_button.click()
