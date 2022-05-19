from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from POM.Pages.signIn import SignIn
from POM.Pages.dress import CasualDress
from POM.Pages.tShirt import TShirt
from POM.Pages.checkOut import CheckOut
from POM.Pages.signOut import SignOut


s = Service("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://automationpractice.com/index.php")


#login
login=SignIn(driver)
login.click_signIn()
login.enter_email(email="sho@gmail.com")
driver.implicitly_wait(5)
login.enter_password(password="12345")
driver.implicitly_wait(5)
login.click_logIn()


#add a dress
dress=CasualDress(driver)
dress.click_dress()
driver.implicitly_wait(5)
dress.click_casual()
driver.implicitly_wait(5)
dress.click_product()
driver.implicitly_wait(5)
dress.click_cart()
driver.implicitly_wait(5)
dress.click_cross()

#add a shirt
shirt=TShirt(driver)
shirt.click_tShirt()
driver.implicitly_wait(5)
shirt.click_blueColor()
driver.implicitly_wait(5)
shirt.click_product()
driver.implicitly_wait(5)
shirt.click_cart()
driver.implicitly_wait(5)
shirt.click_cross()


#payment by check
pay=CheckOut(driver)
pay.click_shoppingCart()
driver.implicitly_wait(5)
pay.click_proceedCheckOut()
driver.implicitly_wait(5)
pay.click_proceedAddress()
driver.implicitly_wait(5)
pay.click_checkbox()
driver.implicitly_wait(5)
pay.click_proceedShipping()
driver.implicitly_wait(5)
pay.click_payByCheck()


#signout
signOut = SignOut(driver)
signOut.click_signOut()
time.sleep(2)

driver.close()
print("test completed for User1")
