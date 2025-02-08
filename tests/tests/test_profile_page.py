import pytest
from ..page_objects.login_page import LoginPage
from ..page_objects.profile_page import ProfilePage


@pytest.mark.smoke
def test_login_user(open_login_page, get_user_name, get_user_password):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password)
    ProfilePage(open_login_page).find_exit_href()


@pytest.mark.sanity
def test_change_subscribe_email(get_subscribe_page, get_user_test_email):
    get_subscribe_page.driver.refresh()
    get_subscribe_page.set_new_email(get_user_test_email). \
        click_change_email(). \
        find_success_message(). \
        check_success_message()


@pytest.mark.sanity
def test_activate_subscribe(get_subscribe_page):
    get_subscribe_page.subscribe()
    assert get_subscribe_page.check_subscribe == 'yes'


@pytest.mark.sanity
def test_deactivate_subscribe(get_subscribe_page):
    get_subscribe_page.unsubscribe()
    assert get_subscribe_page.check_subscribe == 'no'
