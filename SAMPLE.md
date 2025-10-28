# 🎬 Parabank UI Test Automation Sample

This project demonstrates UI test automation using Playwright with Python and Page Object Model (POM) pattern, targeting the [Parabank demo application](https://parabank.parasoft.com/parabank/index.htm).

## 🎯 What's Covered

### 1. Login Flow Tests (`test_parabank_login.py`)

- ✅ Page load verification
- ✅ Valid login (using demo credentials)
- ✅ Invalid login error handling
- ✅ Form validation for empty fields

### 2. Account Overview Tests (`test_parabank_overview.py`)

- ✅ Account list verification
- ✅ Navigation to account details
- ✅ Account services menu validation
- 🔄 New account creation (planned)

## 🏗️ Project Structure

```
playwright-automation/
├── pages/                  # Page Object Models
│   ├── parabank_login_page.py
│   ├── account_overview_page.py
│   └── transfer_funds_page.py
├── tests/                  # Test Suites
│   ├── test_parabank_login.py
│   └── test_parabank_overview.py
├── utils/
│   └── config.py          # Configuration (BASE_URL, etc.)
└── reports/               # Test Reports
```

## 🔧 Page Objects

### Login Page (`parabank_login_page.py`)

```python
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

### Account Overview Page (`account_overview_page.py`)

```python
class AccountOverviewPage:
    def __init__(self, page):
        self.page = page
        self.header = page.locator("h1.title:has-text('Accounts Overview')")
        self.accounts_table = page.locator("table#accountTable")

    def account_ids(self) -> List[str]:
        links = self.page.locator("table#accountTable a")
        return [t.strip() for t in links.all_text_contents()]
```

## 🚀 Quick Start

1. **Setup Virtual Environment**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. **Install Playwright Browsers**

```powershell
playwright install
```

3. **Run Tests**

```powershell
# All tests
pytest tests/ -v

# Specific test suite
pytest tests/test_parabank_login.py -v

# Single test with debug
$env:PWDEBUG=1
pytest tests/test_parabank_login.py::test_parabank_valid_login -v
```

## 🔑 Test Credentials

- Default demo account:
  - Username: `john`
  - Password: `demo`

For custom credentials:

```powershell
$env:PARABANK_USERNAME = "your_username"
$env:PARABANK_PASSWORD = "your_password"
```

## 📋 Test Coverage

| Feature          | Status      | Notes                                  |
| ---------------- | ----------- | -------------------------------------- |
| Login            | ✅ Complete | Basic auth, validation, error handling |
| Account Overview | ✅ Complete | List accounts, navigation              |
| Funds Transfer   | 🔄 Planned  | POM ready, tests pending               |
| Bill Pay         | 📋 Backlog  | Not started                            |

## 🔍 Debug Tips

1. **Visual Debugging**

   - Use `PWDEBUG=1` for Playwright Inspector
   - Screenshots saved on test failure in `reports/screenshots/`

2. **HTML Reports**

```powershell
pytest --html=reports/report.html
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests following existing patterns
4. Ensure all tests pass
5. Submit pull request

## 📚 Resources

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Parabank Demo App](https://parabank.parasoft.com/parabank/index.htm)
- [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
