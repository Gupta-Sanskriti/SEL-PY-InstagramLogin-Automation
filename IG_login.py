# without action chains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.instagram.com/")

# Xpaths & variables
login_id = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
password = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
submit_btn = driver.find_element(By.XPATH,"//*[@id='loginForm']/div/div[3]/button/div")
not_now = driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div/div/div/button")

time.sleep(5)
# actions.send_keys(password,"hello")
login_id.send_keys("")#enter your user name here
password.send_keys("") #enter your password
submit_btn.click()
time.sleep(3)
# not_now.click()


today = time.timezone
print(today)

# pressing enter -- submit_btn
# actions.click(submit_btn)
# actions.perform()



