
from selenium.webdriver.common.by import By
class SignIn():
    def __init__(self,driver):
        self.driver = driver

        self.signIn_button_className = "login"
        self.email_textBox_id = "email"
        self.password_textBox_id = "passwd"
        self.logIn_button_id = "SubmitLogin"

    def click_signIn(self):
        self.driver.find_element(By.CLASS_NAME, self.signIn_button_className).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.email_textBox_id).click()
        self.driver.find_element(By.ID, self.email_textBox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_textBox_id).click()
        self.driver.find_element(By.ID, self.password_textBox_id).send_keys(password)
    def click_logIn(self):
        self.driver.find_element(By.ID, self.logIn_button_id).click()



