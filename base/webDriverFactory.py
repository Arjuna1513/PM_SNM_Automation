from selenium import webdriver
class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def get_driver_instance(self):
        if self.browser == "ie":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get("http://10.211.162.111/mp")
        driver.implicitly_wait(10)
        return driver