import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


class api():

    def __init__(self, driver):
        self.driver = driver

    def api_request(self):
        time.sleep(3)
        for request in self.driver.requests:
            if request.response.status_code > 304:
                return(
                    request.url,
                    request.response.status_code,
                    request.response.headers['Content-Type']
                )
            else:
                return True

