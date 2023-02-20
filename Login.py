from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.jumia.co.ke/")

login_button = driver.find_element_by_xpath("//a[@href='/customer/account/login/']")
login_button.click()

email_field = driver.find_element_by_id("login")
password_field = driver.find_element_by_id("password")
email_field.send_keys("abc@gmail.com")
password_field.send_keys("password123")

submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()

time.sleep(5)

welcome_message = driver.find_element_by_xpath("//div[contains(text(),'Welcome back')]")
assert "Welcome back" in welcome_message.text

driver.quit()





