import time

from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_register(driver):
    driver.get("https://automationexercise.com/login")
    assert "login" in driver.current_url

    login_page = LoginPage(driver)
    login_page.input_name(name_input="Aglamkhujayeva Ruxshona")
    login_page.input_email(email_address="aglamkhujayevaruxshona@gmail.com")
    login_page.click_button()
    time.sleep(2)
    error_text = login_page.get_error_message()

    if "Email Address already exist!" in error_text:
        print("User already exists. Trying to log in...")

        login_page.saved_email("aglamkhujayevaruxshona@gmail.com")
        login_page.saved_password("13072024zalatoy")
        login_page.click_login()
        time.sleep(2)

        login_page.click_test_cases_btn()
        assert "test_cases" in driver.current_url
        return

    elif "signup" in driver.current_url:
        print("New user registration flow.")
        signup_page = SignupPage(driver)

        signup_page.click_gender_radio_button()
        get_name = signup_page.get_input_name()
        assert get_name == "Aglamkhujayeva Ruxshona"
        get_email = signup_page.get_input_email()
        assert get_email == "aglamkhujayevaruxshona@gmail.com"
        signup_page.input_password("13072024zalatoy")
        signup_page.click_day(option_name='21')
        signup_page.click_month(option_name='March')
        signup_page.click_year(option_name='2006')
        signup_page.click_newsletter_checkbox()
        signup_page.input_information("Ruxshona")
        signup_page.input_information("Aglamkhujayeva")
        signup_page.input_information("DelxIt Group")
        signup_page.input_information("Kumushbuloq Street")
        signup_page.input_information("Rohat City")
        signup_page.click_country_dropdown(option_name="Canada")
        signup_page.input_information("Tashkent")
        signup_page.input_information("Tashkent")
        signup_page.input_information("1000095")
        signup_page.input_information("998507062650")
        signup_page.click_btn()
        return

    else:
        raise AssertionError("Signup ham bo‘lmadi, login ham bo‘lmadi. Muammo mavjud!")
