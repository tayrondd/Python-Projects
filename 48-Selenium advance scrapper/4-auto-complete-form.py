from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service(r"C:\Users\tds030\Downloads\Files\app\python-projects\48-selenium\chromedriver.exe")

#this stop chrome to close automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
url = "https://web.archive.org/web/20211121100453/http://secure-retreat-92358.herokuapp.com/"
driver.get(url)


fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Tayron")

lName = driver.find_element(By.NAME, "lName")
lName.send_keys("De los santos")

email = driver.find_element(By.NAME, "email")
email.send_keys("tay231@hotmail.com")

submit = driver.find_element(By.TAG_NAME, "button")
submit.send_keys(Keys.ENTER)