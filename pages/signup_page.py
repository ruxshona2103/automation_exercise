from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):
    # ------------------------------------------------------------------------------------------------------------------
    GENDER_RADIO_BUTTON = (By.XPATH, '//input[@id="id_gender2"]')
    GET_NAME_INPUT = (By.XPATH, '//input[@id="name"]')
    GET_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    DAY_DROPDOWN = (By.XPATH, '//select[@id="days"]')
    MONTH_DROPDOWN = (By.XPATH, '//select[@id="months"]')
    YEAR_DROPDOWN = (By.XPATH, '//select[@id="years"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//input[@id="newsletter"]')
    INPUT_FIRST_NAME = (By.ID, 'first_name')
    INPUT_LAST_NAME = (By.ID, 'last_name')
    INPUT_COMPANY = (By.ID, 'company')
    INPUT_ADRESS_1 = (By.ID, 'address1')
    INPUT_ADRESS_2 = (By.ID, 'address2')
    COUNTRY_DROPDOWN = (By.ID, 'country')
    INPUT_STATE = (By.ID, 'state')
    INPUT_CITY = (By.ID, 'city')
    INPUT_ZIPCODE = (By.ID, 'zipcode')
    INPUT_MOBILE_PHONE = (By.ID, 'mobile_number')
    CLICK_CREATE_ACC = (By.XPATH, '//button[@data-qa="create-account"]')
    # ------------------------------------------------------------------------------------------------------------------

    def click_gender_radio_button(self):
        self.click(self.GENDER_RADIO_BUTTON)

    def get_input_name(self):
        return self.get_input_text(self.GET_NAME_INPUT)

    def get_input_email(self):
        return self.get_input_text(self.GET_INPUT_EMAIL)

    def input_password(self, password):
        self.input_text(self.INPUT_PASSWORD, password)

    def click_day(self, option_name):
        self.click_option(self.DAY_DROPDOWN, option_name=option_name)

    def click_month(self, option_name):
        self.click_option(self.MONTH_DROPDOWN, option_name)

    def click_year(self, option_name):
        self.click_option(self.YEAR_DROPDOWN, option_name)

    def click_newsletter_checkbox(self):
        self.click(self.NEWSLETTER_CHECKBOX)

    def input_information(self,input_information):
        self.input_text(self.INPUT_FIRST_NAME, input_information)
        self.input_text(self.INPUT_LAST_NAME, input_information)
        self.input_text(self.INPUT_COMPANY, input_information)
        self.input_text(self.INPUT_ADRESS_1, input_information)
        self.input_text(self.INPUT_ADRESS_2, input_information)
        self.input_text(self.INPUT_STATE, input_information)
        self.input_text(self.INPUT_CITY, input_information)
        self.input_text(self.INPUT_ZIPCODE, input_information)
        self.input_text(self.INPUT_MOBILE_PHONE, input_information)

    def click_country_dropdown(self, option_name):
        self.click_option(self.COUNTRY_DROPDOWN, option_name)

    def click_btn(self):
        self.click(self.CLICK_CREATE_ACC)