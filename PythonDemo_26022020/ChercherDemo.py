'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import actions

driver=webdriver.Chrome("C:\driver\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
'''
sorc=driver.find_element_by_id("sub-menu")
actions = ActionChains(driver)

hover = actions.move_to_element(sorc)
hover.perform()
driver.find_element_by_id('link2').click()
'''
#actions.move_to_element()
        # find the element
menu = driver.find_element_by_id("sub-menu")
google_link=driver.find_element_by_id("link2")
        #Create the object for Action Chains
actions = ActionChains(driver)
actions.move_to_element(menu).move_to_element(google_link).click(google_link).perform()
driver.back()
actions1 = ActionChains(driver)
double_click99=driver.find_element_by_id("double-click")
actions1.double_click(double_click99).perform()
alert = driver.switch_to_alert()
str1=alert.text
print(str1)
alert.accept()

# perform the operation on the element
#actions.perform()
