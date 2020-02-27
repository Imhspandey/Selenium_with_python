'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/droppable/");
driver.switch_to.frame(0)
sorc= driver.find_element_by_id("draggable")
tgt=driver.find_element_by_id("droppable")
        
actions = ActionChains(driver)

actions.drag_and_drop(sorc, tgt).perform()