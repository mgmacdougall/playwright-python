import pytest
from pathlib import Path
from utils import config


@pytest.fixture(scope="session")
def base_url():
    """Base URL for tests, can be overridden with the BASE_URL env var."""
    return config.BASE_URL


# Save a screenshot for failed test calls when the `page` fixture is available
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = Path("reports/screenshots")
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            filename = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(filename))
