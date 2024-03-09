import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('zina')
        self.element_is_visible(self.locators.EMAIL).send_keys('asd@mail.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("eqwqwff3")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('dsf')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).send_keys('zina')
        email = self.element_is_visible(self.locators.CREATED_EMAIL).send_keys('asd@mail.com')
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).send_keys("eqwqwff3")
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).send_keys('dsf')
        return full_name, email, current_address, permanent_address