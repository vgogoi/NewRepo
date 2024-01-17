from selenium.webdriver.common.by import By
from base.selenium_driver import Selenium_driver
from selenium.webdriver.common.keys import Keys


class RegisterCoursePage(Selenium_driver):
    def __init__(self,driver):
        super().__init__(driver)

    #locators:
    _practicelog_butn = '//a[@data-toggle="dropdown"]'
    _ecommerce_butn = '//li[@data-subid = "11026"]'
    _search_button = '//*[name()="svg" and @xpath="3"]'
    _text_field = 'searchInput'
    _message = '//div[@class = "search-module--searchLabels--a3061" and contains(.,"Search results for ")]/h4'


    def clickOnPracticeBT(self):
        self.ElementClick(self._practicelog_butn,locatorType='xpath')

    def clickOnECommBT(self):
        self.ElementClick(self._ecommerce_butn,locatorType='xpath')

    def NewWindowAction(self):
        self.switchToWindow()
        self.webScroll(direction='down')
        self.webScroll(direction='up')

    def searchProduct(self):
        self.ElementClick(self._search_button,locatorType='xpath')
        self.ElementClick(self._text_field)
        self.send_keys_element('Jeans',self._text_field,locatorType='id')

    def verifyResult(self):
        self.clickOnPracticeBT()
        self.clickOnECommBT()
        self.NewWindowAction()
        self.searchProduct()
        result = self.getElementText(self._message,locatorType='xpath')
        print(result)


