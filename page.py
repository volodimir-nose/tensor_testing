from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 100).until(
            lambda driver: self.driver.find_element(*locator))
        return self.driver.find_element(*locator)



class LoginPage(BasePage):

    def login(self, login, password):
        self.wait_for_element(LoginPageLocators.LOGIN_TEXT_FIELD).send_keys(login)
        self.wait_for_element(LoginPageLocators.PASSWORD_TEXT_FIELD).send_keys(password)
        self.wait_for_element(LoginPageLocators.LOGIN_BUTTON).click()

class OpenStaff(BasePage):

    def staff(self):
        self.wait_for_element(LoginPageLocators.STAFF_LINK).click()