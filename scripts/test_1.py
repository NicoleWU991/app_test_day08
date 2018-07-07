import allure
import pytest


class Test_c:
    @allure.step(title='first test')
    def test_01(self):
        allure.attach('这是描述','这是描述内容')
        print('this is my first item')
        assert True
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_02(self):
        print('this is second item')
        assert False