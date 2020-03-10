from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def func(x):
    return math.log(abs(12 * math.sin(x)))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

def test_wait_my():
    try:
        browser.get(link)
        price_equal_100 = WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
        book_button = browser.find_element_by_id("book")
        book_button.click()
        x = browser.find_element_by_id("input_value")
        data = func(int(x.text))
        input_field = browser.find_element_by_id("answer")
        input_field.send_keys(str(data))
        submit = browser.find_element_by_id("solve")
        submit.click()
        time.sleep(7)
    finally:
        browser.quit()
