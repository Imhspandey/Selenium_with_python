'''
Created on Feb 26, 2020

@author: training_d5.01.02
'''
from selenium import webdriver
import time
from _ast import Assert

driver = webdriver.Chrome("C:\driver\chromedriver.exe")
driver.maximize_window()
location = "//C:/Users/training_d5.01.02/Documents/prompt_alert.htm"
driver.get(location)

#Click on the "employeeLogin" button to generate the Prompt Alert
button = driver.find_element_by_name('employeeLogin')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

time.sleep(2)

#Enter text into the Alert using send_keys()
obj.send_keys('pravin singh')

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )
# Assert.assertEqual(message,"You have logged in successfully !!")

time.sleep(2)

obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)
# Assert.assertEquals(txt,"Welcome pravin singh!! How can I help you?")

driver.close




