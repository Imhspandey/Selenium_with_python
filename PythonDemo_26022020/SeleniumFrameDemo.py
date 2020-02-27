'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time


driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to.frame("classFrame")

driver.find_element_by_xpath("//html/body/div[3]/table/tbody[2]/tr[1]/td[1]/a").click()
time.sleep(10)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//html/body/div/ul/li[1]/a").click()

