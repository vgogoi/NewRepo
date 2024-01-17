from selenium.webdriver.common.by import By
from base.selenium_driver import Selenium_driver

class LoginPage(Selenium_driver):
    def __init__(self,driver):
        super().__init__(driver)

    #locators
    _login_link = '//a[@href="/login"]'
    _email_field = 'email'
    _pwd_field = 'login-password'
    _login_buttn = 'login'
    _error_login = '//span[@class="error"]'


    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH,self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.NAME,self._email_field)
    #
    # def getPwdField(self):
    #     return self.driver.find_element(By.NAME,self._pwd_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID,self._login_buttn)

    def clickLoginButtn(self):
        self.ElementClick(self._login_buttn)

    def clickLoginLink(self):
        self.ElementClick(self._login_link,locatorType='xpath')

    def enterUsrName(self,email):
        self.send_keys_element(email,self._email_field)

    def enterPwd(self,pwd):
        self.send_keys_element(pwd,self._pwd_field)


    def login(self,email='',pwd=''):
        self.clickLoginLink()
        self.enterUsrName(email)
        self.enterPwd(pwd)
        self.clickLoginButtn()


    def error_login(self):
        self.waitForElement(self._error_login,locatorType='xpath')
        result = self.elementPresenceCheck(self._error_login,locatorType='xpath')
        return result


