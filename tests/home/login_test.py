from pages.home.login_page import LoginPage
from pages.courses.course_page import Course_page
import unittest
import pytest

@pytest.mark.usefixtures('onetimesetup','setup')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, onetimesetup):
        self.lp = LoginPage(self.driver)
        self.co = Course_page(self.driver)

    @pytest.mark.run(order =2)
    def test_validlogin(self):
        self.lp.login('mikgogoi@gmail.com','Meditation@1234')
        self.co.checkFullCoursetest()
    @pytest.mark.run(order = 1)
    def test_invalidlogin(self):
        self.lp.login('mikgogoi@gmaiasddal.com', 'Meditation@1234asd')
        result = self.lp.error_login()
        assert result == True









