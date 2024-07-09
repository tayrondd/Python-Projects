from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chrome_driver_path = Service(r"C:\Users\tds030\Downloads\Files\app\python-projects\48-Selenium advance scrapper\chromedriver.exe")

#this stop chrome to close automatically
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
url = "https://www.linkedin.com/"
driver.get(url)
sleep(1)

# handling linkedin login
email = "tay1234@hotmail.com"
password = ""

username = driver.find_element(By.NAME, "session_key")
username.send_keys(email)
passw = driver.find_element(By.NAME, "session_password")
passw.send_keys(password)
sign_in = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button') #sign in button
sign_in.click()

#handling job application auto complete
url_2 = "https://www.linkedin.com/jobs/search/?currentJobId=3507296736&f_AL=true&f_WT=2&keywords=python"
driver.get(url_2)
sleep(2)
driver.find_element(By.CLASS_NAME, "job-card-container").click()
sleep(2)
driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()

# Phone country code 
phone_select = Select(driver.find_element(By.XPATH, '//*[@id="text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3586046246-87592931-phoneNumber-country"]'))
phone_select.select_by_visible_text("Dominican Republic (+1)")

#Mobile phone number
phone_number = driver.find_element(By.CLASS_NAME, " artdeco-text-input--input")
phone_number.send_keys("1234567891")

driver.find_element(By.ID, "ember591").click()
sleep(1)
driver.find_element(By.ID, "ember591").click()
