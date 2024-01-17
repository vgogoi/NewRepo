from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from traceback import print_stack
import utilities.custom_logger as cl
import logging


class Selenium_driver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info('Locator Type ' + locatorType + ' not available')
        return False

    def getElement(self,locator,locatorType = 'id'):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info('Element found with locator:' + locator + ' and locator-type:' + locatorType )
        except:
            self.log.info('Element not found with locator:' + locator + ' and locator-type:' + locatorType)
        return element

    def ElementClick(self,locator,locatorType = 'id'):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info('Clicked on element with locator: ' + locator + ' and locator type: '+ locatorType)
        except:
            self.log.info('Cannot click on element')

    def send_keys_element(self,data,locator,locatorType = 'id'):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info('Sent data on element with locator: ' + locator + ' and locator type: '+ locatorType)
        except:
            self.log.info('Cannot send data on element')

    def send_keys_element_submit(self,data,locator,locatorType = 'id'):
        try:
            element = self.getElement(locator,locatorType)
            element.send_keys(data).submit()
            self.log.info('Sent data on element with locator: ' + locator + ' and locator type: '+ locatorType)
        except:
            self.log.info('Cannot send data on element')

    def isElementPresent(self,locator,locatorType='id'):
        try:
            element = self.driver.find_element(locator,locatorType)
            if element is not None:
                self.log.info('Element found')
                return True
            else:
                self.log.info('Element not found')
                return False
        except:
            self.log.info('Element not found')
            return False

    def getElementText(self,locator,locatorType):
        element = None
        try:
            element = self.getElement(locator,locatorType).text
            self.log.info('Text present')
        except:
            self.log.info('Text not present')
        return element


    def elementPresenceCheck(self,locator,locatorType):
        element = self.getElement(locator, locatorType)
        try:
            if element is not None:
                self.log.info('Element found using ' + locatorType)
                return True
            else:
                self.log.info('Element not found using ' + locatorType)
                return False
        except:
            self.log.info('Element not found using ' + locatorType)
            return False

    def waitForElement(self,locator,locatorType='id',timeout=10,pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info('Waiting for max time:: '+ str(timeout))

            wait = WebDriverWait(self.driver,10,poll_frequency=1)
            element = wait.until(EC.element_to_be_clickable((byType,locator)))
            self.log.info('Element appeared')
        except:
            self.log.info('Element didnot appear')
        return element

    def webScroll(self,direction = 'up'):
        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0, 1000);")


    def switchToWindow(self):
        try:
            all_handles = self.driver.window_handles
            print(all_handles)
            self.log.info('##### All window handles #####')
            new_win = all_handles[1]
            self.driver.switch_to.window(new_win)


        except:
            self.log.info('Couldnt switch to NewWindow')


            # 100716835229
            # 101227543174
