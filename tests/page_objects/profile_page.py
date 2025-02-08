from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from ..page_objects.base_page import BasePage
from ..page_objects.locators.profile_page import Locators


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def find_exit_href(self, timeout=3):
        self._element_is_visible(locator=(By.XPATH, self.locators.href_exit_xpath_locator), timeout=timeout)
        return self

    def click_exit(self, timeout=3):
        self._click_button(locator=(By.XPATH, self.locators.href_exit_xpath_locator), timeout=timeout)
        return self

    def set_new_email(self, test_email):
        message = self.driver.find_element(by=By.NAME, value=self.locators.email_input_name_locator)
        self.driver.execute_script("arguments[0].value = '';", message)  # clear element with java script
        self._fill_input(test_email, (By.NAME, self.locators.email_input_name_locator))
        return self

    def click_change_email(self):
        self._click_button((By.XPATH, self.locators.button_change_email_xpath_locator))
        return self

    def find_success_message(self):
        self._element_is_visible(locator=(By.XPATH, self.locators.change_email_message_xpath_locator))
        return self

    def check_success_message(self):
        success_message = self.driver.find_element(by=By.XPATH, value=self.locators.change_email_message_xpath_locator)
        assert success_message.text == 'Well Done'
        return self

    @property
    def check_subscribe(self):
        state_subscribe = self.driver.find_element(by=By.XPATH,
                                                   value=self.locators.state_subscribe_message_xpath_locator)
        if state_subscribe.text == 'Yes':
            state_subscribe = 'yes'
        else:
            state_subscribe = 'no'
        return state_subscribe

    def subscribe(self):
        if self.check_subscribe == 'yes':
            self._click_button((By.XPATH, self.locators.button_deactivate_subscribe_xpath_locator))
            self._click_button((By.XPATH, self.locators.button_activate_subscribe_xpath_locator))
            self.driver.refresh()
        elif self.check_subscribe == 'no':
            self._click_button((By.XPATH, self.locators.button_activate_subscribe_xpath_locator))
            self.driver.refresh()
        return self

    def unsubscribe(self):
        if self.check_subscribe == 'yes':
            self._click_button((By.XPATH, self.locators.button_deactivate_subscribe_xpath_locator))
            self.driver.refresh()
        elif self.check_subscribe == 'no':
            self._click_button((By.XPATH, self.locators.button_activate_subscribe_xpath_locator))
            self._click_button((By.XPATH, self.locators.button_deactivate_subscribe_xpath_locator))
            self.driver.refresh()
        return self
