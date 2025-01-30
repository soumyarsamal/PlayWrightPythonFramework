
import pytest

from playwrightpython.utils.credential_management import LoginCredentials
from playwrightpython.utils.json_validator import JsonResponseValidator


@pytest.mark.smoke
def test_get_api(api_client):
    #Login.login_as(LoginCredentials.OPERATOR)
    print("Operator Username:", LoginCredentials.OPERATOR.username)
    print("Operator Password:", LoginCredentials.OPERATOR.password)
    print("Senior Operator Username:", LoginCredentials.SENIOR_OPERATOR.username)
    print("Senior Operator Password:", LoginCredentials.SENIOR_OPERATOR.password)
    response = api_client.get("/api/users?page=2")
    assert response.status_code == 200
    print(response.json())
    JsonResponseValidator(response.json()) \
    .assert_json("$.total_pages", 2) \
    .assert_json("$.total", 12)
    assert "data" in response.json()

@pytest.mark.demo
def test_get_api_by_id(api_client):
    response = api_client.get("2")
    assert response.status_code == 200
    print(response.json())
    # JsonResponseValidator(response.json()) \
    # .assert_json("$.total_pages", 2) \
    # .assert_json("$.total", 12)
    # assert "data" in response.json()
