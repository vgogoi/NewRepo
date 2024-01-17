import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.yield_fixture
def setup():
    print('Running method level setUp')
    yield
    print('Running method level Teardown')

@pytest.yield_fixture(scope='class')
def onetimesetup(request):
    print('Running one time setUp')
    base_url = 'https://www.letskodeit.com/'
    serv_obj = Service('/Users/vineetgogoi/Downloads/chromedriver-mac-x64/chromedriver')
    driver = webdriver.Chrome(service=serv_obj)
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(3)
    print('Running Chrome')

    request.cls.driver = driver
    yield driver
    driver.quit()
    print('Teardown method running')


