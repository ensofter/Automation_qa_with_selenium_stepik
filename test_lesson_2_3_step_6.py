import time
import math
from selenium import webdriver

def func(x):
    return math.log(abs(12 * math.sin(x)))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

def test_lesson6():
    try:
        click_button = browser.find_element_by_tag_name("button")
        click_button.click()
        new_tab = browser.window_handles[1]
        browser.switch_to.window(new_tab)
        x = browser.find_element_by_id("input_value").text
        data = func(int(x))
        input_fild = browser.find_element_by_id("answer")
        input_fild.send_keys(str(data))
        submit = browser.find_element_by_tag_name("button")
        submit.click()
        time.sleep(8)

    finally:
        browser.quit()
