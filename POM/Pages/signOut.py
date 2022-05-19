from selenium.webdriver.common.by import By
class SignOut():
    def __init__(self,driver):
        self.driver = driver

        self.signOut_button_className ="logout"
    def click_signOut(self):
        self.driver.find_element(By.CLASS_NAME, self.signOut_button_className ).click()