class Locators:
    username_input_name_locator = 'USER_LOGIN'  # Name of element
    password_input_name_locator = 'USER_PASSWORD'  # Name of element
    email_input_name_locator = 'USER_EMAIL'  # Name of element
    login_btn_xpath_locator = '/html/body/div/div/form/button'  # x-path locator
    href_exit_xpath_locator = '/html/body/div[1]/div/a'
    error_message_xpath_locator = '//font[@class="errortext"]'
    forgot_your_password_xpath_locator = '//A[@class="color_tmp"][@href="/personal/profile/index.php?forgot_password=yes"][text()="Password is broken"]'
