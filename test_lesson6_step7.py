from selenium import webdriver
import time

def test_form():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    fields = browser.find_elements_by_xpath("//input[@type='text']")
    for el in fields:
        el.send_keys("asdfg")
    submit_button = browser.find_element_by_css_selector(".btn.btn-default")
    submit_button.click()
    time.sleep(30)
