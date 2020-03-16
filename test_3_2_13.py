from selenium import webdriver
import unittest


class TestNewTestCase(unittest.TestCase):

    def test_registration(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.name = self.browser.find_element_by_css_selector("[placeholder='Input your first name']")
        self.name.send_keys("Alexei")
        self.last = self.browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        self.last.send_keys("Romashov")
        self.email = self.browser.find_element_by_css_selector('[placeholder="Input your email"]')
        self.email.send_keys("asd@asdd.com")
        self.submit = self.browser.find_element_by_tag_name("button")
        self.submit.click()
        self.h1 = self.browser.find_element_by_tag_name("h1")
        self.phrase = self.h1.text
        self.assertEquals(self.phrase, 'Congratulations! You have successfully registered!', 'Some error')
        self.browser.quit()

    def test_registration2(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.name = self.browser.find_element_by_css_selector('[qplaceholder="Input your name"]')
        self.name.send_keys("Alex")
        self.email = self.browser.find_element_by_css_selector('[placeholder="Input your email"]')
        self.email.send_keys("aasdf")
        self.submit = self.browser.find_element_by_tag_name("button")
        self.submit.click()
        self.h1 = self.browser.find_element_by_tag_name("h1")
        self.phrase = self.h1.text
        self.assertEquals(self.phrase, 'Congratulations! You have successfully registered!', 'Some error')
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
