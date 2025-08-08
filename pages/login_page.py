from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    NAME_INPUT = (By.XPATH, '//form[@action="/signup"]//input[@name="name"]')
    EMAIL_INPUT = (By.XPATH, '//form[@action="/signup"]//input[@name="email"]')
    SIGN_UP_BUTTON = (By.XPATH, '//form[@action="/signup"]//button[@data-qa="signup-button"]')
    ERROR_MSG = (By.XPATH, "//p[text()='Email Address already exist!']")
    SAVED_EMAIL = (By.XPATH, '//input[@data-qa="login-email"]')
    SAVED_PASSWORD = (By.XPATH, '//input[@data-qa="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@data-qa="login-button"]')
    TEST_CASES_BTN = (By.XPATH, '//button[@class="btn btn-success"]')

    #     ------------------------------------------------------------------------------------------------------------------

    def input_name(self, name_input):
        self.input_text(self.NAME_INPUT, name_input)

    def input_email(self, email_address):
        self.input_text(self.EMAIL_INPUT, email_address)

    def click_button(self):
        self.click(self.SIGN_UP_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

#     ------------------------------------------------------------------------------------------------------------------

    def saved_email(self, saved_email):
        self.input_text(self.SAVED_EMAIL, saved_email)

    def saved_password(self, saved_password):
        self.input_text(self.SAVED_PASSWORD, saved_password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_test_cases_btn(self):
        self.click(self.TEST_CASES_BTN)