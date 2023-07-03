from selenium import webdriver
from pages.main_page import Main_page
from pages.search_img_page import Search_img_page
from pages.search_text_page import Search_page


def test_search_company():
    driver = webdriver.Chrome()
    driver.maximize_window()
    main = Main_page(driver)
    main.search_company()
    sp = Search_page(driver)
    sp.search_text_page()


def test_search_img():
    driver = webdriver.Chrome()
    driver.maximize_window()
    mp = Main_page(driver)
    mp.search_img()
    sip = Search_img_page(driver)
    sip.img_page()
