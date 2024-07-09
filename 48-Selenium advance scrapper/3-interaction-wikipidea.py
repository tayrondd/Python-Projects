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
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)


# articles_qty = driver.find_element(By.CSS_SELECTOR, "#articlecount a") # selecter "articlecount" ID and the "a" TAG
# articles_qty = articles_qty.get_attribute("innerHTML")
# print(articles_qty)

# driver.find_element(By.XPATH, '//*[@id="p-search"]/a').click()
search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)