from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.jumia.co.ke/')
cart_icon = driver.find_element_by_xpath('//a[@href="/cart/"]')
cart_icon.click()
cart_icon = driver.find_element_by_xpath('//a[@href="/cart/"]')
cart_icon.click()
cart_items = driver.find_elements_by_xpath('//div[@class="checkout-item -product"]')
for item in cart_items:
    print("Item is removed from the cart")
driver.quit()