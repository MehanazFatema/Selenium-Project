from selenium.webdriver.common.by import By
class TShirt():
    def __init__(self,driver):
        self.driver = driver

        self.tShirt_button_xPath = '//*[@id="block_top_menu"]/ul/li[3]/a'
        self.blue_color_xPath = '//*[@id="layered_id_attribute_group_14"]'
        self.select_product_xPath= '//*[@id="center_column"]/ul/li'
        self.add_cart_id="add_to_cart"
        self.cross_cart_className="cross"


    def click_tShirt(self):
        self.driver.find_element(By.XPATH, self.tShirt_button_xPath).click()

    def click_blueColor(self):
        self.driver.find_element(By.XPATH, self.blue_color_xPath).click()

    def click_product(self):
        self.driver.find_element(By.XPATH, self.select_product_xPath).click()
    def click_cart(self):
        self.driver.find_element(By.ID, self.add_cart_id).click()
    def click_cross(self):
        self.driver.find_element(By.CLASS_NAME, self.cross_cart_className).click()
