from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started...")  
driver=webdriver.Chrome()
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element_by_name("q").send_keys("python tutorials") 
driver.find_element_by_name("q").send_keys(Keys.ENTER) 
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
#close the browser  
driver.close()  
print("sample test case successfully completed")  
