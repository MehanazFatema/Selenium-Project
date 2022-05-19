from selenium.webdriver.common.by import By
class CheckOut():
    def __init__(self,driver):
        self.driver = driver

        self.cart_button_xPath = '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
        self.proceed_checkout_xPath = '//*[@id="center_column"]/p[2]/a[1]'
        self.proceed_address_xPath= '//*[@id="center_column"]/form/p/button'
        self.check_box_xPath='//*[@id="cgv"]'
        self.proceed_shipping_xPath = '//*[@id="form"]/p/button'
        self.payment_xPath='//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a'



    def click_shoppingCart(self):
        self.driver.find_element(By.XPATH, self.cart_button_xPath ).click()

    def click_proceedCheckOut(self):
        self.driver.find_element(By.XPATH, self.proceed_checkout_xPath).click()
    def click_proceedAddress(self):
        self.driver.find_element(By.XPATH, self.proceed_address_xPath).click()
    def click_checkbox(self):
        self.driver.find_element(By.XPATH, self.check_box_xPath).click()

    def click_proceedShipping(self):
        self.driver.find_element(By.XPATH, self.proceed_shipping_xPath).click()

    def click_payByCheck(self):
        self.driver.find_element(By.XPATH, self.payment_xPath).click()