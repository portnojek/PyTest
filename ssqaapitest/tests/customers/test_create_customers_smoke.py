'''
to bywa pomocne
pytest -h => a potem:
pytest -m tcid29 -s --log-cli-level=debug
i w pliku pytest.ini dodajemy zapisy takie:

log_cli = true
log_cli_level = debug
obczaj jeszcze co oznacza: python setup.py develop
'''
import pytest
import logging as logger
from ssqaapitest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqaapitest.src.helpers.customers_helper import CustomerHelper

@pytest.mark.tcid29
def test_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")
    logger.debug("TEST: Create new customer with email and password only")
    rand_info = generate_random_email_and_password()
    logger.info(rand_info)

    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    import pdb; pdb.set_trace()

    # verify satus code of the call

    # verify email in the response

    # verify customer is created in database



