import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def test_sum_two_int():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        cifer1 = browser.find_element_by_id("num1")
        cifer1_int = int(cifer1.text)
        cifer2 = browser.find_element_by_id("num2")
        cifer2_int = int(cifer2.text)
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(str(cifer1_int + cifer2_int))
        submit_button = browser.find_element_by_tag_name("button")
        submit_button.click()
    finally:
        time.sleep(15)
        browser.quit()
