from testui.elements.testui_element import e
from cv_pom.cv_pom_driver import CVPOMDriver

class ContactUs:
    def __init__(self, driver, cv_driver: CVPOMDriver):
        self.name_field =  e(driver, "id", "name")
        self.email_field = e(driver, "id", "email")
        self.message = e(driver, "id", "message")
        # CV Elements
        # self.name_field_cv = cv_driver.element({"text": {"value": "Full Name", "case_sensitive": False}})
        # self.email_field_cv = cv_driver.element({"text": {"value": "Business E-mail", "case_sensitive": False, "contains": True}})
        # self.message_cv = cv_driver.element({"text": {"value": "Message", "case_sensitive": False, "contains": True}})

        self.name_field_cv = cv_driver.element({"label": {"value": "name"}})
        self.email_field_cv = cv_driver.element({"label": {"value": "email"}})
        self.message_cv = cv_driver.element({"label": {"value": "message"}})

    def fill_all_form_details(self):
        self.name_field.send_keys("John Doe")
        self.email_field.send_keys("johndoe@example.com")
        self.message.send_keys("This is a test message")

    def fill_all_form_details_cv(self):
        self.name_field_cv.swipe_to("down").send_keys("John Doe")
        self.email_field_cv.swipe_to("down").send_keys("johndoe@example.com")
        self.message_cv.swipe_to("down").send_keys("This is a test message")
