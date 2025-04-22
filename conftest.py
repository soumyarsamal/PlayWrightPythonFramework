import json
import os

import pytest
from playwright.sync_api import sync_playwright

from playwrightpython.pages.login import LoginService
from playwrightpython.utils.api_helpers import APIClient
from playwrightpython.utils.credential_management import load_credentials, LoginCredentials
from playwrightpython.utils.database_credential import load_db_credentials, DBDetails, DBCredDetails


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="function")
def browser(playwright_instance):
    launch_options = {"headless": False, "slow_mo": 0}
    browser = playwright_instance.chromium.launch(**launch_options, args=['--start-maximized'])
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def api_base_url(config):
    return config["base_uri"]  # Provide the base URL from the config


@pytest.fixture(scope="session")
def api_client(api_base_url):
    return APIClient(base_url=api_base_url)


VALID_ENVIRONMENTS = ["dev7", "ift"]


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev7",
        choices=VALID_ENVIRONMENTS,  # Restrict choices to valid environments
        help="Specify the environment to run tests against (e.g., dev7, ift, ift1)"
    )


# Fixture to load the environment-specific configuration
@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")  # Get the environment from command line
    # common environment level properties
    config_file_path = os.path.join(f"playwrightpython/config/{env}", f"{env}.json")
    environment = 'ift' if 'ift' in env else 'dev'

    # common login credential for dev and ift
    credential_file_path = os.path.join("playwrightpython/config", f"{environment}_login_credential.json")

    # common DB credential for dev and ift
    db_cred_file_path = os.path.join("playwrightpython/config", f"{environment}_db_credential.json")

    credentials_data = load_credentials(credential_file_path)
    LoginCredentials.initialize(credentials_data)

    db_data = load_db_credentials(config_file_path)
    DBDetails.initialize(db_data)

    db_credentials_data = load_db_credentials(db_cred_file_path)
    DBCredDetails.initialize(db_credentials_data)

    if not os.path.exists(config_file_path):
        pytest.exit(f"Configuration file not found for environment: {env}")

    with open(config_file_path, "r") as file:
        return json.load(file)


@pytest.fixture(scope="session")
def ui_base_url(config):
    return config["url"]  # Provide the base URL from the config


@pytest.fixture
def logged_in_user(request, page, ui_base_url):
    # Check the marker passed to the test
    role = None
    if 'operator' in request.node.keywords:
        role = LoginCredentials.OPERATOR
    elif 'senior_operator' in request.node.keywords:
        role = LoginCredentials.SENIOR_OPERATOR

    if role:
        login_service = LoginService(page, ui_base_url)
        return login_service.login_as(role)
    else:
        pytest.fail("No valid role found in test marker")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot on test failure
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Create directory if it doesn't exist
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            test_name = item.name.replace("/", "_").replace(":", "_")
            filepath = os.path.join(screenshot_dir, f"{test_name}.png")
            page.screenshot(path=filepath)
            print(f"\n📸 Screenshot saved to {filepath}")
