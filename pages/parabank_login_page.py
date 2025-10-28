"""Page object for Parabank login page (https://parabank.parasoft.com)."""
from playwright.sync_api import Page


class ParabankLoginPage:
    def __init__(self, page: Page):
        self.page = page
        # Parabank uses name attributes for username/password
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        # Button can be an input or button element depending on markup
        self.login_button = page.locator("input[value='Log In'], button:has-text('Log In')")

    def goto(self, base_url: str = "https://parabank.parasoft.com/parabank/index.htm") -> None:
        """Navigate to the Parabank login page."""
        self.page.goto(base_url)

    def login(self, username: str, password: str) -> None:
        """Perform login using the provided credentials.

        Args:
            username: Parabank username
            password: Parabank password
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
