from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def test_cptcha():

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        treasure = browser.find_element_by_id("treasure")
        x = treasure.get_attribute("valuex")
        formula = calc(x)

        input = browser.find_element_by_id("answer")
        input.send_keys(formula)

        checkbox_im_the_robot = browser.find_element_by_css_selector("input[id='robotCheckbox']")
        checkbox_im_the_robot.click()

        people_radio = browser.find_element_by_id("peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked is not None, "People radio is not selected by default"


        radio_robot_rule = browser.find_element_by_css_selector("input[id='robotsRule']")
        radio_robot_rule.click()

        button = browser.find_element_by_css_selector("button[type='submit']")
        button.click()

        time.sleep(5)

    finally:
        time.sleep(2)
