from selenium import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

print("sample test case started...")

## To open chrome browser
object_1 = webdriver.Chrome()

## To maximize broser
object_1.maximize_window()

## to open url
object_1.get("https://www.hotstar.com/in")
time.sleep(3)

## to click movies button
moveies=object_1.find_element_by_xpath("//div[contains(text(),'Movies')]")
action = ActionChains(object_1);
action.move_to_element(moveies).perform()
time.sleep(5)

##  select tamil movies
object_1.find_element_by_xpath("//a[text()='Tamil']").click()
time.sleep(5)

## get text from element

content=object_1.find_element_by_xpath("//h2[contains(text(),'Popular in Tamil Movies')]").text
print("content=",content)

## reload web page
object_1.refresh()
time.sleep(2)

## to close broser
object_1.close()



