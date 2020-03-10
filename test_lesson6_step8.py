from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

def test_input_form():

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_name("first_name")
        first_name.send_keys("Aleksey")
        last_name = browser.find_element_by_name("last_name")
        last_name.send_keys("Romashov")
        city = browser.find_element_by_css_selector(".form-control.city")
        city.send_keys("Saint-Petersburg")
        country = browser.find_element_by_id("country")
        country.send_keys("Russia")
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()

    finally:
        time.sleep(30)

        browser.quit()


