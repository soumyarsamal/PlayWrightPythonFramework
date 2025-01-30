import pytest

from playwrightpython.database.connection_manager import fetch_data_from_postgres
from playwrightpython.pages.home_page import HomePage
from playwrightpython.utils.config import BASE_URL


@pytest.mark.UI
def test_title_check(page):
    home_page = HomePage(page)
    home_page.navigate(BASE_URL)
    assert home_page.gettext() == "ProtoCommerce"


@pytest.mark.operator
@pytest.mark.logincheck
def test_login(logged_in_user):
    query = "SELECT * FROM public.passenger_info;"
    data = fetch_data_from_postgres(query)
    print(data)
    print(data[0]['p_id'])
    logged_in_user.check_if_landed_on_homePage()
    pass