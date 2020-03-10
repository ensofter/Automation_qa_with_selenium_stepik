from selenium import webdriver

url = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()

def test_explicit():
    try:
        browser.get(url)
        button = browser.find_element_by_id("button")

    finally:
        browser.quit()
