from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = Service(r"C:\Users\tds030\Downloads\Files\app\python-projects\48-selenium\chromedriver.exe")

#this stop chrome to close automatically
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=chrome_driver_path, chrome_options=chrome_options)

driver = webdriver.Chrome(service=chrome_driver_path)
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
driver.get(url)


# get text by css selector 
# price = driver.find_element(By.CSS_SELECTOR, "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span.a-offscreen")
# print(price.get_attribute("innerHTML"))

# get text by xpath
# price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[1]')
# print(price.get_attribute("innerHTML"))

# get text by class name
price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.get_attribute("innerHTML"))