import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_userlogin:


    def test_userlogin_001(self):
        a=5
        b=6
        sum=a+b
        print(sum)
        if sum==11:
            assert True
        else:
            assert False

    def test_userlogin_002(self):
        a = 5
        b = 6
        sum = a + b
        print(sum)
        if sum == 15:
            assert True
        else:
            assert False

    #
    #
    # def test_login_003(self,):
    #     driver= webdriver.Chrome
    #     driver.get("https://www.instagram.com/accounts/login/")
    #
    #     time.sleep(20)











