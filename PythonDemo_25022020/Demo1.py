'''
Created on Feb 25, 2020

@author: training_d5.01.02


'''

'''
Created on Feb 25, 2020

@author: training_d5.01.02
'''
''' print("hello python")'''
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(2)
driver.find_element_by_name("btnK").click()
'''
driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TstMeApp/fetchcat.htm")