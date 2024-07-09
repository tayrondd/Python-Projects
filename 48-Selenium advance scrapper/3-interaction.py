from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(r"C:\Users\tds030\Downloads\Files\app\python-projects\48-selenium\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

articles_qty = driver.find_element(By.CSS_SELECTOR, "#articlecount a") # selecter "articlecount" ID and the "a" TAG
articles_qty = articles_qty.get_attribute("innerHTML")

print(articles_qty)