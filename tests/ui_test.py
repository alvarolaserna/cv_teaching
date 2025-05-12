import pytest
from selenium.webdriver.chrome.options import Options
from testui.support.appium_driver import NewDriver, TestUIDriver
from cv_pom.frameworks import TestUICVPOMDriver
from cv_pom.cv_pom_driver import CVPOMDriver
from testui.elements.testui_element import e
from tests.pages.google_page import GooglePage
from pathlib import Path


@pytest.fixture(autouse=True)
def testui_driver():
    options = Options()
    options.add_argument("disable-user-media-security")
    options.add_argument("--force-device-scale-factor=1")
    # options.add_argument("--headless")
    driver = NewDriver().set_selenium_driver(chrome_options=options)

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def cv_pom_driver(testui_driver):
    BASE_DIR = Path(__file__).resolve().parent
    model_path = BASE_DIR / "resources" / "best_g.pt" 
    driver = TestUICVPOMDriver(model_path, testui_driver)
    yield driver


class TestSuite:
    def test_test_for_testdevlab(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        testui_driver.navigate_to("https://testdevlab.com")
        testui_driver.get_driver().set_window_size(1200, 700)
        # Prompt: click on Accept
        e(testui_driver, "css", ".CookieManagement_actions__XrYwF button").click()
        # Prompt: click in contact us
        e(testui_driver, "css", 'a[href="/contact-us"]').click()
        # Prompt: enter random credentials in Full name, Business E-mail and Message
        # Enter random credentials in Full Name
        e(testui_driver, "id", "name").send_keys("John Doe")
        # Enter random credentials in Business E-mail
        e(testui_driver, "id", "email").send_keys("johndoe@example.com")
        # Enter random credentials in Message
        e(testui_driver, "id", "message").send_keys("This is a test message")


    def test_test_for_testdevlab_cv(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        testui_driver.navigate_to("https://testdevlab.com")
        testui_driver.get_driver().set_window_size(1200, 700)
        # Prompt: click in contact us
        cv_pom_driver.element({"text": {"value": "Contact us", "case_sensitive": False}}).click()
        # Prompt: click on Accept
        cv_pom_driver.element({"text": "Accept"}).click()
        # Prompt: enter random credentials in Full name, Business E-mail and Message
        # Enter random credentials in Full Name
        cv_pom_driver.element({"text": {"value": "Full Name", "case_sensitive": False}}).send_keys("John Doe")

        # Enter random credentials in Business E-mail
        cv_pom_driver.element({"text": {"value": "Business E-mail", "case_sensitive": False, "contains": True}}).swipe_to("down").send_keys("johndoe@example.com")

        # Enter random credentials in Message
        cv_pom_driver.element({"text": {"value": "Message", "case_sensitive": False, "contains": True}}).swipe_to("down").send_keys("This is a test message")


    def test_test_for_google_cv(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        testui_driver.navigate_to("https://google.com")
        GooglePage(cv_pom_driver).click_cookies().all_actions()
