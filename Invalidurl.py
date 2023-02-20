from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()
invalid_url = "https://thisisnotavalidurl.com"
try:
    driver.get(invalid_url)
except WebDriverException as e:
    print(f"Error: {e}")

driver.quit()
