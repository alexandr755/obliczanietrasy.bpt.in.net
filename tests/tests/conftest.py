from time import time
from pytest import fixture
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from ..utils.config_manager import ConfigManager
from ..utils.driver_factory import DriverFactory
from ..page_objects.profile_page import ProfilePage
from ..page_objects.login_page import LoginPage

from ..utils.config_manager import ROOT_PATH


@fixture(scope='session')
def get_driver() -> WebDriver:
    driver = DriverFactory(ConfigManager.browser).get_driver()
    yield driver
    driver.quit()


@fixture
def open_login_page(get_driver) -> WebDriver:
    get_driver.get(ConfigManager.url_profile)
    get_driver.maximize_window()
    return get_driver


@fixture
def get_logged_profile_page(open_login_page, get_user_name, get_user_password) -> ProfilePage:
    try:
        return ProfilePage(open_login_page).find_exit_href(timeout=1)  # check if profile page is opened
    except TimeoutException:
        LoginPage(open_login_page).do_login(get_user_name, get_user_password)
        return ProfilePage(open_login_page)


@fixture
def get_subscribe_page(open_login_page, get_logged_profile_page):
    ProfilePage(open_login_page.get(ConfigManager.url_subscribe))
    return ProfilePage(open_login_page)

@fixture
def open_info_page(get_driver) -> WebDriver:
    get_driver.get(ConfigManager.url_info)
    get_driver.maximize_window()
    return get_driver

@fixture(scope='session')
def get_user_name() -> str:
    return ConfigManager.user_name


@fixture(scope='session')
def get_user_password() -> str:
    return ConfigManager.user_pass


@fixture(scope='session')
def get_user_name_incorrect() -> str:
    return ConfigManager.user_name_incorrect


@fixture(scope='session')
def get_user_password_incorrect() -> str:
    return ConfigManager.user_pass_incorrect


@fixture(scope='session')
def get_user_test_email() -> str:
    return ConfigManager.test_email
