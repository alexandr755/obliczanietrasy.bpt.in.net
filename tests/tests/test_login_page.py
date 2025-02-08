import pytest
from ..page_objects.login_page import LoginPage
from ..page_objects.profile_page import ProfilePage


@pytest.mark.smoke
def test_successful_authorization(open_login_page, get_user_name, get_user_password):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password)
    ProfilePage(open_login_page).find_exit_href().click_exit()


@pytest.mark.sanity
def test_user_login_incorrect(open_login_page, get_user_name_incorrect, get_user_password):
    LoginPage(open_login_page).do_login(get_user_name_incorrect, get_user_password). \
        find_error_message(). \
        check_error_message()


@pytest.mark.sanity
def test_user_password_incorrect(open_login_page, get_user_name, get_user_password_incorrect):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password_incorrect). \
        find_error_message(). \
        check_error_message()


@pytest.mark.sanity
def test_empty_fields_in_form(open_login_page, get_user_name='', get_user_password=''):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password). \
        find_error_message(). \
        check_error_message()


@pytest.mark.sanity
def test_password_recovery(open_login_page):
    LoginPage(open_login_page). \
        click_forgot_pass(). \
        find_field_email()
