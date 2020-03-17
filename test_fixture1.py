from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite...")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nquit browser for test suite...")
        self.browser.quit()

    def test_guest_shloud_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

class TestMainPage2():
    def setup_method(self):
        print("\nstart browser for test...")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nquit browser for test...")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

