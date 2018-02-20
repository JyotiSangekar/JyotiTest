from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.get('https://unomaha.instructure.com/courses/8916/assignments/61462')
print ('UNO page opened up')
driver.implicitly_wait(3)

username = driver.find_element_by_id('username')
username.send_keys('jsangekar')
password = driver.find_element_by_class_name('UnoPassword')
password.send_keys('Bioinf0!')
login = driver.find_element_by_name("_eventId_proceed")
login.click()
print('Yes! you logged into jyotis prfile')
time.sleep(3)

syllabus=driver.find_element_by_link_text("Syllabus")
syllabus.click()
print ('Clicked home icon on left of the page')

elm= driver.find_element_by_link_text("Act 3")
elm.click()
print ('We are ready to re-submit activity 3')

