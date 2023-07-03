from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://ya.ru/"
    search_word = "Тензор"

    # Locators
    id_input_search = "text"
    xpath_suggest_block = "//ul[@class='mini-suggest__popup-content']"
    xpath_items_more = "//a[@title='Все сервисы']"
    xpath_img_button = "//a[@aria-label='Картинки']"

    # Getters
    def get_input_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.id_input_search)))

    def get_suggest_block(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xpath_suggest_block)))

    def get_items_more(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.xpath_items_more)))

    def get_img_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xpath_img_button)))

    # Actions
    def send_input_search(self):
        self.get_input_search().send_keys(self.search_word)
        print("Send keys to input")

    def visibility_of_input_search(self):
        try:
            visibility_of(self.get_input_search())
            print("Input search is visible")
        except TimeoutException:
            print("Input search is  not visible")

    def visibility_of_suggest_block(self):
        try:
            visibility_of(self.get_suggest_block())
            print("Suggest block is visible")
        except TimeoutException:
            print("Suggest block is  not visible")

    def visibility_of_items_more(self):
        try:
            visibility_of(self.get_items_more())
            print("Button of items  is visible")
        except TimeoutException:
            print("Button of items  is  not visible")

    def enter_input_search(self):
        self.get_input_search().send_keys(Keys.ENTER)
        print("Enter")

    def click_input_search(self):
        self.get_input_search().click()
        print("Click to input")

    def click_items_more(self):
        self.get_items_more().click()
        print("Click button of items")

    def click_img_button(self):
        self.get_img_button().click()
        print("Click button of image")

    # Methods
    def search_company(self):
        Logger.add_start_step(method="search_company")
        self.driver.get(self.url)
        self.get_current_url()
        self.visibility_of_input_search()
        self.send_input_search()
        self.visibility_of_suggest_block()
        self.enter_input_search()
        Logger.add_end_step(method="search_company")

    def search_img(self):
        Logger.add_start_step(method="search_img")
        self.driver.get(self.url)
        self.visibility_of_items_more()
        self.click_input_search()
        self.visibility_of_items_more()
        self.click_items_more()
        self.click_img_button()
        Logger.add_end_step(method="search_img")
