from selenium import webdriver
import time

def test_example():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        first_name.send_keys("Aleksey")
        second_name = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        second_name.send_keys("Romashov")
        email = browser.find_element_by_css_selector(".form-control.third")
        email.send_keys("amromashov@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_allert = browser.find_element_by_tag_name("h1")
        assert "Congratulations! You have successfully registered!" == welcome_allert.text


    finally:
        time.sleep(5)
        browser.quit()
