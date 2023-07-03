from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Search_img_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Assert messages
    good_assert_input = "Value of category and value of search input are same. OK"
    bad_assert_input = "Value of category and value of search input are  not same. NOT OK"



    # Locators
    xpath_left_side_of_media_viewer = "//div[@class='SwipeImage-Side SwipeImage-Side_side_left']"
    xpath_src_img = "//img[@class='MMImage-Origin']"
    xpath_media_viewer = "//div[@class='MediaViewer-View MediaViewer_theme_fiji-View']"
    xpath_to_prev_page = "//div[@class='CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button " \
                         "MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev " \
                         "MediaViewer_theme_fiji-ButtonPrev']"
    xpath_to_next_page = "//div[@class='CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button " \
                         "MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonNext " \
                         "MediaViewer_theme_fiji-ButtonNext']"
    xpath_focused_first_img = "img[@class='SimpleImage-Image SimpleImage-Image_clickable']"
    xpath_first_img = "//div[@class='serp-item__preview']"
    xpath_input_img_search = "//input[@name='text']"
    xpath_first_category = "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']"
    xpath_name_of_first_category = "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']/a/div[2]"

    # Getters
    def get_first_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xpath_first_category)))

    def get_tag_of_first_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_name_of_first_category)))

    def get_input_img_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.xpath_input_img_search)))

    def get_first_img(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.xpath_first_img)))

    def get_to_next_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_to_next_page)))

    def get_to_prev_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_to_prev_page)))

    def get_media_viewer(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_media_viewer)))

    def get_left_side_of_media_viewer(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_left_side_of_media_viewer)))

    # Actions
    def change_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def click_first_category(self):
        self.get_first_category().click()

    def get_name_of_first_category(self):
        return self.get_tag_of_first_category().get_attribute("innerHTML")

    def get_text_from_input_img_search(self):
        return self.get_input_img_search().get_attribute("value")

    def click_to_first_img(self):
        self.get_first_img()[0].click()

    def move_cursor_to_image_view(self):
        media_viewer = self.get_media_viewer()
        action = ActionChains(self.driver)
        action.move_to_element(media_viewer)
        action.perform()

    def click_to_next_page(self):
        self.get_to_next_page().click()

    def move_cursor_to_left_side_of_image_view(self):
        media_viewer = self.get_left_side_of_media_viewer()
        action = ActionChains(self.driver)
        action.move_to_element(media_viewer).perform()

    def click_to_prev_page(self):

        # action.perform()
        self.get_to_prev_page().click()

    def visibility_of_view_img(self):
        try:
            visibility_of(self.get_media_viewer())
            print("Image viewer is visible")
        except TimeoutException:
            print("Image is  not visible")

    def src_img1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_src_img))).get_attribute("src")

    def src_img2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_src_img))).get_attribute("src")

    def src_img1_prev(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_src_img))).get_attribute("src")

    def mismatch_assertion(self, word, result, msg):
        value_word = word
        assert value_word != result
        print(msg)

    # Methods

    def img_page(self):
        Logger.add_start_step(method="img_page")
        self.change_window()
        self.assert_url("https://yandex.ru/images/")
        self.click_first_category()
        self.assert_word(self.get_name_of_first_category(), self.get_text_from_input_img_search(), self.good_assert_input, self.bad_assert_input)
        self.click_to_first_img()
        self.visibility_of_view_img()
        image_first = self.src_img1()
        self.move_cursor_to_image_view()
        self.click_to_next_page()
        image_second = self.src_img2()
        self.mismatch_assertion(image_first, image_second, "Image changed")
        self.move_cursor_to_left_side_of_image_view()
        self.click_to_prev_page()
        image_first_prev = self.src_img1_prev()
        self.assert_word(image_first, image_first_prev, "In step №11 Image is same like in step №8", "NOT SAME PICTURES.NOT OK")
        Logger.add_end_step(method="img_page")
