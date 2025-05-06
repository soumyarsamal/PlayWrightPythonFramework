import allure
import pytest

from playwrightpython.database.connection_manager import fetch_data_from_postgres
from playwrightpython.utils.credential_management import LoginCredentials
from playwrightpython.utils.json_validator import JsonResponseValidator


@allure.feature("API test")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.smoke
def test_get_api(api_client):
    # Login.login_as(LoginCredentials.OPERATOR)
    with allure.step("running api test"):
        query = "SELECT * FROM public.passenger_info;"
        data = fetch_data_from_postgres(query)
        print(data)
        print(data[0]['p_id'])

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
    with allure.step("running api test"):
        response = api_client.get("2")
        assert response.status_code == 200
        print(response.json())
    # JsonResponseValidator(response.json()) \
    # .assert_json("$.total_pages", 2) \
    # .assert_json("$.total", 12)
    # assert "data" in response.json()
