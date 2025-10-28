# 🧪 Parabank Test Automation with Playwright Python

This repository contains a UI test automation framework for [Parabank](https://parabank.parasoft.com/parabank/index.htm) built with [Playwright for Python](https://playwright.dev/python/), following the Page Object Model (POM) design pattern.

## 📦 Project Structure

```
playwright-automation/
├── tests/
│   └── test_parabank_login.py
├── pages/
│   ├── parabank_login_page.py
│   ├── account_overview_page.py
│   └── transfer_funds_page.py
├── utils/
│   └── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

- `tests/`: Test cases for Parabank functionality
- `pages/`: Page Object classes for Parabank pages
- `utils/`: Configuration and utilities
- `conftest.py`: Pytest fixtures and hooks
- `pytest.ini`: Test configuration
- `requirements.txt`: Python dependencies

## 🚀 Getting Started

### 1. Create a virtual environment and install dependencies

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Install Playwright browsers

```powershell
playwright install
```

### 3. Run tests

```powershell
# Run all Parabank tests
pytest tests/test_parabank_login.py -v

# Run a specific test
pytest tests/test_parabank_login.py::test_parabank_login_page_loads -v

# Run with HTML report
pytest tests/test_parabank_login.py -v --html=reports/report.html
```

## 🧱 Page Object Model (POM)

Each page class encapsulates selectors and actions for a specific Parabank page:

```python
# pages/parabank_login_page.py
class ParabankLoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("input[value='Log In']")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
```

## 🧪 Sample Test

```python
# tests/test_parabank_login.py
def test_parabank_login_page_loads(page: Page, base_url: str):
    """Test that the Parabank login page loads and contains expected elements."""
    login_page = ParabankLoginPage(page)
    login_page.goto(base_url)

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()
```

## Environment Variables

For login tests with real credentials:

```powershell
$env:PARABANK_USERNAME = "your_username"
$env:PARABANK_PASSWORD = "your_password"
pytest tests/test_parabank_login.py::test_parabank_valid_login -v
```

## 🛠️ Configuration

Use `pytest.ini` to configure test options:

```ini
[pytest]
addopts = --headed --slowmo=50
```

## 📚 Useful Commands

Debug with Playwright inspector:

```powershell
$env:PWDEBUG = "1"
pytest tests/test_parabank_login.py
```

## 📖 References

- [Parabank Demo Site](https://parabank.parasoft.com/parabank/index.htm)
- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Docs](https://docs.pytest.org/)
- [Page Object Model Guide](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

Run Tests:

# Run all Parabank tests

pytest tests/test_parabank_login.py -v

# Run a specific test

pytest tests/test_parabank_login.py::test_parabank_login_page_loads -v

# Run with HTML report

pytest tests/test_parabank_login.py -v --html=reports/report.html

$env:PARABANK_USERNAME = "your_username"
$env:PARABANK_PASSWORD = "your_password"
pytest tests/test_parabank_login.py::test_parabank_valid_login -v

# Run all overview tests

pytest tests/test_parabank_overview.py -v

# Run a specific test

pytest tests/test_parabank_overview.py::test_account_list_not_empty -v

# Run with custom credentials

$env:PARABANK_USERNAME = "your_username"
$env:PARABANK_PASSWORD = "your_password"
pytest tests/test_parabank_overview.py -v
