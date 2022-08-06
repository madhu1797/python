from selenium import *
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

## To open web broser
driver=webdriver.Chrome()

## to maxixize window
driver.maximize_window()

## open particular link
driver.get("https://chercher.tech/practice/table")
time.sleep(2)

## To get row length
row=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr")
row=len(row)
print(row)

time.sleep(2)
## to get col length
col=len(driver.find_elements_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[2]/td"))
print(col)

## Extract table values
print("Website"+"          "+"Title"+"          "+"Field")
for r in range (2, row+1):
	for c in range (1, col+1):
		value=(driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr["+str(r)+"]/td["+str(c)+"]")).text
		print(value,end='           ')
	print()

time.sleep(2)
driver.close()
