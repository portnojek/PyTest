import pytest

pytestmark = [pytest.mark.fe, pytest.mark.smoke]

@pytest.fixture()
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")


@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user():
    print("Login with valid user")
    print("Function: aaaaaaaa")
    assert 2==2, "Bug"

@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbbbb")


