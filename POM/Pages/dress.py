from selenium.webdriver.common.by import By
class CasualDress():
    def __init__(self,driver):
        self.driver = driver

        self.dress_button_xPath = '//*[@id="block_top_menu"]/ul/li[2]/a'
        self.casual_button_xPath = '//*[@id="categories_block_left"]/div/ul/li[1]/a'
        self.select_product_xPath= '//*[@id="center_column"]/ul/li/div'
        self.add_cart_id="add_to_cart"
        self.cross_cart_className="cross"


    def click_dress(self):
        self.driver.find_element(By.XPATH, self.dress_button_xPath).click()

    def click_casual(self):
        self.driver.find_element(By.XPATH, self.casual_button_xPath).click()

    def click_product(self):
        self.driver.find_element(By.XPATH, self.select_product_xPath).click()

    def click_cart(self):
        self.driver.find_element(By.ID, self.add_cart_id).click()

    def click_cross(self):
        self.driver.find_element(By.CLASS_NAME, self.cross_cart_className).click()

