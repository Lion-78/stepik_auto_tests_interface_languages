from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button(browser):
    browser.get(link)
    time.sleep(15)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "button is missing"

#  pytest --language=fr test_items.py
