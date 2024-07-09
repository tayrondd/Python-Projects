from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service(r"C:\Users\tds030\Downloads\Files\app\python-projects\48-selenium\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://www.python.org/"
driver.get(url)

list = {}

for x in range(1, 6):
    date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{x}]/time')
    name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{x}]/a')
    
    date = date.get_attribute("datetime")[:+10] #[:+10] just take the first 1- characters from the left
    name = name.get_attribute("innerHTML")
    list.update({x-1:{
        "time": date,
        "name":name
    }})
    
print(list)

# another way to get date using css selector .event-widget as class, time as a tag
# date = driver.find_element(By.CSS_SELECTOR, ".event-widget time")
# date = date.get_attribute("datetime")[:+10]
# print(date)
