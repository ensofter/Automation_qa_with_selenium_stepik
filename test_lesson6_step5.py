from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

def test_find_element_by_text():

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        print("\n", link_text)
        ahref = browser.find_element_by_link_text(link_text)
        ahref.click()

        first_name = browser.find_element_by_name("first_name")
        first_name.send_keys("Aleksey")
        last_name = browser.find_element_by_name("last_name")
        last_name.send_keys("Romashov")
        city = browser.find_element_by_css_selector(".form-control.city")
        city.send_keys("SPB")
        country = browser.find_element_by_id("country")
        country.send_keys("Russia")
        button = browser.find_element_by_tag_name("button")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()
