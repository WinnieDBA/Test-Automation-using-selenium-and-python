from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.jumia.co.ke/")

search_box = driver.find_element_by_name("")
search_box.send_keys("")
search_box.send_keys(Keys.RETURN)

product = driver.find_element_by_xpath("//div[@class='sku -gallery']//a[@class='core']") # assuming the first product in search results
product.click()

add_to_cart = driver.find_element_by_xpath("//div[@class='info-section']//button[@class='btn _prim _md _icn _with-icon add-to-cart']") 
add_to_cart.click()

checkout_button = driver.find_element_by_xpath("//a[@class='btn _prim checkout-button']") 
checkout_button.click()
ling address, and payment method
fullname = driver.find_element_by_name("fullname")
fullname.send_keys("Customer Full Name")

email = driver.find_element_by_name("email")
email.send_keys("customer@email.com")

phone = driver.find_element_by_name("phone")
phone.send_keys("Customer Phone Number")

address = driver.find_element_by_name("address")
address.send_keys("Customer Address")
driver.close()
