import pytest


pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.fixture(scope='module')
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")

    return{'id': 20, 'name': "Bartek"}

@pytest.mark.abc
class TestCheckout(object):

    def test_checkout_as_guest(self, my_setup):
        print("checkout as guest")
        print("Class: 1111111")


    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")
        print("Class: 2222222")

#uruchamianie takiego skryptu: pytest -m abc -s
#pytest --html=demo_report.html - generowanie htmla (wymaga biblioteki pytest-html)
#pytest --html=demo_report.html --self-contained-html
