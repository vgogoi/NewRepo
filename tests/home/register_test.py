from pages.courses.register_course_page import RegisterCoursePage
import unittest
import pytest

@pytest.mark.usefixtures('onetimesetup','setup')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, onetimesetup):
        self.rtt = RegisterCoursePage(self.driver)
    @pytest.mark.run(order =1)
    def test_1(self):
        self.rtt.verifyResult()

