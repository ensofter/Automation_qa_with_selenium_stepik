import time
import math
from selenium import webdriver

def func(x):
    return math.log(abs(12 * math.sin(x)))

def test_alert():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/alert_accept.html")
        button = browser.find_element_by_tag_name("button")
        button.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        x = browser.find_element_by_id("input_value").text
        data = func(int(x))
        input_field = browser.find_element_by_id("answer")
        input_field.send_keys(str(data))
        submit = browser.find_element_by_css_selector("[type='submit']")
        submit.click()
        time.sleep(5)

    finally:
        browser.close()
