import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "//input[@type='email']"
    _password_field = "//input[@type='password']"
    _login_button = "//button[contains(text(),'Login')]"
    _tutoril = "//a[@class='introjs-skipbutton']"

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def tutoril(self):
        self.waitForElement(self._tutoril, locatorType="xpath")
        self.elementClick(self._tutoril, locatorType="xpath")

    def delete_api_request(self):
        del self.driver.requests


    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.tutoril()
        self.delete_api_request()
        time.sleep(2)
