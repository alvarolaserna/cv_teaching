from testui.elements.testui_element import e
from tests.pages.contact_us_tdl import ContactUs
from cv_pom.cv_pom_driver import CVPOMDriver

class LandingPage:
    def __init__(self, driver, cv_driver: CVPOMDriver):
        self.driver = driver
        self.cv_driver = cv_driver
        self.contact_us_button = e(driver, "css", 'a[href="/contact-us"]')
        self.accept_cookies_button = e(driver, "css", ".CookieManagement_actions__XrYwF button")
        # CV Elements
        # self.accept_cookies_button_cv = cv_driver.element({"text": {"value": "Contact us", "case_sensitive": False}})
        # self.contact_us_button_cv = cv_driver.element({"text": "Accept"})
        # CV Elements
        self.accept_cookies_button_cv = cv_driver.element({"label": {"value": "cookies"}})
        self.contact_us_button_cv = cv_driver.element({"label": "contact-us"})

    def accept_cookies(self):
        self.accept_cookies_button.click()

        return self
    
    def accept_cookies_cv(self):
        self.accept_cookies_button_cv.click()

        return self

    def go_to_contact_us(self):
        self.contact_us_button.click()

        return ContactUs(self.driver, self.cv_driver)
    
    def go_to_contact_us_cv(self):
        self.contact_us_button_cv.click()

        return ContactUs(self.driver, self.cv_driver)

