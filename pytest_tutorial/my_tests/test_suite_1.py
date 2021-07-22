import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]

@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")

    return{'id': 20, 'name': "Bartek"}

@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(my_setup):
    print("Login with valid user")
    print("Function: aaaaaaaa")
    assert 2==2, "Bug"
    print("Name: {}".format(my_setup.get('name')))
    # import pdb; pdb.set_trace() - jakiś debuger (do weryfikacji jeszcze o co w tym chodzi)

@pytest.mark.regression
def test_login_page_wrong_password():
    print("Login with wrong password")
    print("Function: bbbbbbbb")


