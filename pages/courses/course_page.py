from base.selenium_driver import Selenium_driver
from selenium.webdriver.common.by import By
from base.selenium_driver import Selenium_driver


class Course_page(Selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _my_course_link = "//h1[@class='dynamic-heading']"
    _all_course_link = '//li[@data-id=''41189'']/a'
    _all_course_text = '//h1[@class="dynamic-heading margin-bottom-20"]'
    _usr_icon = '//*[@id="header5"]/div/nav/div/div[1]/a/img'

    def retrieve_text(self):
        text = self.getElementText(self._my_course_link, locatorType='xpath')
        print(text)

    def clickAllcourses(self):
        self.ElementClick(self._all_course_link, locatorType='xpath')

    def checkTextinCourses(self):
        text = self.getElementText(self._all_course_text, locatorType='xpath')
        print(text)

    def checkusrIcon(self):
        result = self.elementPresenceCheck(self._usr_icon, locatorType='xpath')
        if result:
            print('Icon appearing')
        return result

    def checkFullCoursetest(self):
        self.retrieve_text()
        self.clickAllcourses()
        self.checkTextinCourses()
        self.checkusrIcon()




