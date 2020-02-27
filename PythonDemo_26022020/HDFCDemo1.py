'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time


driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/?_ga=2.22962107.1698599154.1582690639-2146895405.1582690639")
driver.switch_to_frame("login_page")
driver.find_element_by_name("fldLoginUserId").send_keys("Him7882087")
time.sleep(2)
#driver.find_element_by_xpath("//input[@name='fldLoginUserId']").send_keys("Himanshu2087")
driver.find_element_by_xpath("//img[@alt='continue']").click()
driver.switch_to_default_content()
driver.switch_to_frame(1)
driver.find_element_by_link_text("Privacy Policy").click()