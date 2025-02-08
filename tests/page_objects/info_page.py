from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from ..page_objects.base_page import BasePage
from ..page_objects.locators.info_page import Locators


class InfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def get_menu_items(self) -> list[str]:
        return self.get_texts(locator=(By.XPATH, self.locators.menu_items_xpath_locator))