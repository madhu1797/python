
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


print("sample test case started")

##To Initiate chrome browser


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("facebook log in")
driver.find_element_by_name("q").send_keys(Keys.ENTER)


driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/table/tbody/tr[2]/td[1]/div/span/h3/a')
                               
##driver.find_element(By.XPATH, '//button[text()="Some text"]')
##driver.find_element(By.text("Sign Up For Facebook®")).send_keys(Keys.ENTER)


print("sample test case successfully completed")

