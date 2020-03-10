from selenium import webdriver
import time
import os

def test_lesson9():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/file_input.html")
        first_name = browser.find_element_by_name("firstname")
        first_name.send_keys("Alex")
        last_name = browser.find_element_by_name("lastname")
        last_name.send_keys("Narayan")
        email = browser.find_element_by_name("email")
        email.send_keys("asd@asd.com")
        input_file = browser.find_element_by_name("file")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')
        input_file.send_keys(file_path)
        button = browser.find_element_by_tag_name("button")
        button.click()

    finally:
        time.sleep(5)
        browser.quit()
