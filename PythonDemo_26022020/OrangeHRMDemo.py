'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common import actions
import time
driver=webdriver.Chrome("C:\driver\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

time.sleep(3)
Admin=driver.find_element_by_id("menu_admin_viewAdminModule")
User_Management=driver.find_element_by_id("menu_admin_UserManagement")

Users=driver.find_element_by_id("menu_admin_viewSystemUsers")

actions = ActionChains(driver)

actions.move_to_element(Admin).move_to_element(User_Management).click(Users).perform()
