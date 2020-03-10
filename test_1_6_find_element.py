from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

def test_find_element():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element_by_id("submit_button")
        button.click()

    #Закрываем браузер
    finally:
        browser.quit()

def test_find_element_1():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element(By.ID, 'submit_button')
        button.click()

    finally:
        browser.quit()
