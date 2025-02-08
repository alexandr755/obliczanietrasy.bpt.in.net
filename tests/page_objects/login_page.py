from selenium.webdriver.common.by import By

from ..page_objects.base_page import BasePage
from ..page_objects.locators.login_page import Locators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def set_user_name(self, username):
        self._fill_input(username, (By.NAME, self.locators.username_input_name_locator))
        return self

    def set_password(self, password):
        self._fill_input(password, (By.NAME, self.locators.password_input_name_locator))
        return self

    def click_login(self):
        self._click_button((By.XPATH, self.locators.login_btn_xpath_locator))
        return self

    def do_login(self, username, password):
        self.set_user_name(username)
        self.set_password(password)
        self.click_login()
        return self

    def find_error_message(self):
        self._element_is_visible(locator=(By.XPATH, self.locators.error_message_xpath_locator))
        return self

    def check_error_message(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.locators.error_message_xpath_locator)
        assert error_message.text == 'Login or Password are wrong.'
        return self

    def click_forgot_pass(self):
        self._click_button((By.XPATH, self.locators.forgot_your_password_xpath_locator))
        return self

    def find_field_email(self):
        self._element_is_visible(locator=(By.NAME, self.locators.email_input_name_locator))
        return self
