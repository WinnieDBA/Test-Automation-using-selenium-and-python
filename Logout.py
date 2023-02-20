from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.jumia.co.ke/")

login_button = driver.find_element_by_xpath("//a[@href='/customer/account/login/']")
login_button.click()

email_input = driver.find_element_by_name("username")
email_input.send_keys("youremail@example.com")

password_input = driver.find_element_by_name("password")
password_input.send_keys("yourpassword")

login_submit_button = driver.find_element_by_xpath("//button[contains(@class, 'login-btn')]")
login_submit_button.click()

time.sleep(3)  
account_dropdown = driver.find_element_by_xpath("//a[@class='dropdown-toggle']")
account_dropdown.click()

logout_button = driver.find_element_by_xpath("//a[@href='/customer/account/logout/']")
logout_button.click()

time.sleep(3)

driver.quit()
