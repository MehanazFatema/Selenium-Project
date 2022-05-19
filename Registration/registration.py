import readxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("C:\Program Files\chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.maximize_window()
driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(5)

path = "C:/Users/Mehanaz/Desktop/registration.xlsx"
rows=readxl.getRowCount(path,'Sheet1')

for r in range (2, rows+1):
    driver.find_element(By.CLASS_NAME, "login").click()
    driver.implicitly_wait(5)
    email=readxl.readData(path,"Sheet1",r,1)
    firstName = readxl.readData(path, "Sheet1", r, 2)
    lastName = readxl.readData(path, "Sheet1", r, 3)
    password = readxl.readData(path, "Sheet1", r, 4)
    address = readxl.readData(path, "Sheet1", r, 5)
    city = readxl.readData(path, "Sheet1", r, 6)
    zipCode = readxl.readData(path, "Sheet1", r, 7)
    mobile = readxl.readData(path, "Sheet1", r, 8)

    driver.find_element(By.ID,"email_create").send_keys(email)
    driver.find_element(By.ID,"SubmitCreate").click()


    driver.find_element(By.NAME,"customer_firstname").send_keys(firstName)
    driver.find_element(By.NAME,"customer_lastname").send_keys(lastName)
    driver.find_element(By.ID,"passwd").send_keys(password)
    driver.find_element(By.ID,"address1").send_keys(address)
    driver.find_element(By.ID,"city").send_keys(city)

    driver.find_element(By.ID, "id_state").click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH,'//*[@id="id_state"]/option[6]').click()

    driver.find_element(By.ID, "postcode").send_keys(zipCode)
    driver.find_element(By.ID, "phone_mobile").send_keys(mobile)

    driver.implicitly_wait(20)

    driver.find_element(By.ID, "submitAccount").click()
    driver.implicitly_wait(20)

    driver.find_element(By.CLASS_NAME, "logout").click()



driver.close()







