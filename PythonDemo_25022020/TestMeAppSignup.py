'''
Created on Feb 25, 2020

@author: pravin singh
'''

from selenium import webdriver
from select import select
from selenium.webdriver.support.select import Select

import time
driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")
driver.find_element_by_link_text("SignUp").click()
#driver.find_elements_by_class_name("fa fa-lock").click()
#element_by_link_text("RegisterUser.htm").click()
driver.find_element_by_name("userName").send_keys("Himanshu2087")
driver.find_element_by_name("firstName").send_keys("Himanshu")
driver.find_element_by_id("lastName").send_keys("Pandey")
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//img[@alt='Ch']").click()
select1=Select(driver.find_element_by_xpath("//select[@data-handler='selectMonth']"))
select1.select_by_visible_text('May')
select2=Select(driver.find_element_by_xpath("//select[@data-handler='selectYear']"))
select2.select_by_visible_text('1950')
driver.find_element_by_xpath("//a[contains(.,'28')]").click()
select = Select(driver.find_element_by_name('securityQuestion'))
select.select_by_visible_text('What is your Birth Place?')
time.sleep(4)
select.select_by_value("411012")
