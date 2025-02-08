class Locators:
    href_exit_xpath_locator = '//A[@class="__account"][@href="?logout=yes"][text()="Exit"]'
    # username_input_name_locator = 'USER_LOGIN'  # Name of element
    # password_input_name_locator = 'USER_PASSWORD'  # Name of element
    email_input_name_locator = 'EMAIL'  # Name of element
    button_change_email_xpath_locator = '//button[@name="Save"]'
    change_email_message_xpath_locator = '//*[@class ="red"][text()="Well Done"]'
    button_activate_subscribe_xpath_locator = '//*[contains(@class, "custom-btn custom-btn--style-2 unsubscribe")][@name="activate"]'
    button_deactivate_subscribe_xpath_locator = '//*[contains(@class, "custom-btn custom-btn--style-2 unsubscribe")][@name="unsubscribe"]'
    state_subscribe_message_xpath_locator = '//*[@class="data-table"]/descendant::td[text()="Submit is ok"]/following-sibling::td[1]'
