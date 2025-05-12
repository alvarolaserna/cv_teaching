from cv_pom.frameworks import TestUICVPOMDriver

class GooglePage:
    def __init__(self, cv_driver: TestUICVPOMDriver) -> None:
        self.cv_driver = cv_driver
        self.cookies = cv_driver.element({"label": {"value": "cookies"}})
        self.logo = cv_driver.element({"label": {"value": "logo"}})
        self.search = cv_driver.element({"label": {"value": "search"}})
        self.page =  cv_driver.get_page()

    def click_cookies(self):
        try:
            self.cookies.swipe_to('down', limit=4).click()
        except:
            pass

        return self

    def all_actions(self):
        self.logo.wait_visible()
        self.search.send_keys('cv_pom')
        print(self.cv_driver.get_page()._pom.to_json())
        # self.page.element({"text": {"value": "Google Search", "contains": True}}).wait_visible().click()

        return self