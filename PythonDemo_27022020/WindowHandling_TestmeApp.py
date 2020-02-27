'''
Created on Feb 27, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from select import select
from selenium.webdriver.support.select import Select

import time

driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://lkmdemoaut.accenture.com/TestMeApp/fetchcat.htm")

#driver.find_element_by_link_text("SignUp").click()

#driver.find_elements_by_class_name("fa fa-lock").click()
#element_by_link_text("RegisterUser.htm").click()

AboutUS=driver.find_element_by_xpath("//*[@id="menu3"]/li[3]/a/span")
OurOffices=driver.find_element_by_xpath("//*[@id="menu3"]/li[3]/ul/li/a/span")
Chennai=driver.find_element_by_xpath("//*[@id="menu3"]/li[3]/ul/li/ul/li[1]/a/span")

actions = ActionChains(driver)

actions.move_to_element(AboutUS).move_to_element(OurOffices).click(Chennai).perform()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

driver.switch_to_frame("main_page")
contactus = driver.find_element_by_id("demo3")
