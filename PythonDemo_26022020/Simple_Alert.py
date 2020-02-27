'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver

location = '//C:/Users/training_d5.01.02/Documents/simple_alert.htm'
driver=webdriver.Chrome("C:\driver\chromedriver.exe")

driver.implicitly_wait(10)

driver.get(location)

driver.find_element_by_name("alert").click()

driver.switch_to.alert()



