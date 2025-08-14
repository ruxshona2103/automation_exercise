from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    # ------------------------------------------------------------------------------------------------------------------

    def _element_to_be_presence(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return element

    def _element_to_be_visible(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        return element

    def _element_to_be_clickable(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        return element

    def element_scrollable(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    # ------------------------------------------------------------------------------------------------------------------

    def click(self, locator):
        element = self._element_to_be_clickable(locator)
        element.click()

    def wait_for_element(self, locator):
        element = self._element_to_be_visible(locator)
        return element

    def input_text(self, locator, text):
        element = self._element_to_be_visible(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self._element_to_be_visible(locator)
        element = element.text
        return element

    def get_input_text(self, locator):
        element = self._element_to_be_presence(locator)
        value = element.get_attribute("value")
        return value

    def click_option(self, locator, option_name):
        dropdown_element = self._element_to_be_presence(locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_name)

