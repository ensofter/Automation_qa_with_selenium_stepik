from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

def test_explicit_example():
    try:
        browser.get(url)
        button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.ID, 'verify'))
        )
        button.click()
        message = browser.find_element_by_id("verify_message")

        assert "successful" in message.text

    finally:
        browser.quit()

