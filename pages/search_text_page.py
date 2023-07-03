from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Search_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url_start_with = "https://yandex.ru/search/"

    # Locators
    xpath_first_result_on_page = "//li[@data-cid='0']/div/div/a"

    # Getters

    def get_first_result_on_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_first_result_on_page)))

    # Actions
    def check_search_page_url(self):
        if self.get_current_url().startswith(self.url_start_with):
            print("Right search page")
        else:
            print(str(self.get_current_url()))
            print("Wrong search page")

    def assert_first_result(self):
        first_result = self.get_first_result_on_page().get_attribute("href")
        if first_result == "https://tensor.ru/":
            print("First result is TENZOR")
        else:
            print("First result is not TENZOR")

    # Methods
    def search_text_page(self):
        Logger.add_start_step(method="search_text_page")
        self.check_search_page_url()
        self.assert_first_result()
        Logger.add_end_step(method="search_text_page")
