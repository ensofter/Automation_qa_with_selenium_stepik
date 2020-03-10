from selenium import webdriver
import time
import math

def func_1(x):
    return math.log(abs(12 * math.sin(x)))

def test_lesson6():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/execute_script.html")
        x = browser.find_element_by_id("input_value").text
        data = func_1(int(x))
        browser.execute_script("window.scrollBy(0, 100);")
        input_filed = browser.find_element_by_id("answer")
        input_filed.send_keys(str(data))
        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()
        radiobutton = browser.find_element_by_id("robotsRule")
        radiobutton.click()
        button = browser.find_element_by_tag_name("button")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()

