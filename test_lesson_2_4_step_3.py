from selenium import webdriver
import time

url = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()

def test_wait():
    try:
        browser.get(url)
        browser.implicitly_wait(5)
        button = browser.find_element_by_tag_name("button")
        button.click()
        text = browser.find_element_by_id("verify_message").text
        assert text == "Verification was successful!"

    finally:
        browser.quit()

