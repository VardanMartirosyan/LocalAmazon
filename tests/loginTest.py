import time
import unittest
from selenium import webdriver
from pages.signInPage import SignInPage

class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        time.sleep(7)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.signInPageObj = SignInPage(self.driver)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    def test_positive_login(self):
        self.signInPageObj.fill_login_field("vardan98lim@gmail.com")
        time.sleep(2)
        self.signInPageObj.click_to_continue_button()
        time.sleep(2)

        self.signInPageObj.fill_password_field("VardanMartirosyan")
        time.sleep(2)
        self.signInPageObj.click_to_sign_in_button()
        time.sleep(7)

    def tearDown(self) -> None:
        self.driver.close()

