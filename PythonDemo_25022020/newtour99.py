'''
Created on Feb 25, 2020

@author: training_d5.01.02
'''
from selenium import webdriver

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/register.php")
driver.find_element_by_name("firstName").send_keys("Himanshu")
driver.find_element_by_name("lastName").send_keys("Pandey")
driver.find_element_by_xpath("")("lastName").send_keys("Pandey")
select = Select(driver.find_element_by_name('country'))

select.select_by_value("INDIA")




#driver.find_element_by_name("firstName").send_keys("Himanshu")
#driver.find_element_by_id("lastName").send_keys("Pandey")                                                                       ")
#driver.find_element_by_link_text("SignUp").click()