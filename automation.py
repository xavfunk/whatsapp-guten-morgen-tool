from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

contact = "Delas Gruppe" # Omas gruppe
text = "Guten Morgen" # guten Morgen

chrome_options = Options()
chrome_options.add_argument("user-data-dir=/home/xavfunk/.config/google-chrome/Default")

driver = webdriver.Chrome('/home/xavfunk/chromedriver_linux64/chromedriver', options=chrome_options)

driver.get('https://web.whatsapp.com/');

# search contact
inp_xpath_search = "//div[@title='Tekstvak zoekopdracht']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

# select contact
time.sleep(6) # whatsapp starts
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
time.sleep(2)
selected_contact.click() # chat opens

time.sleep(3)

# type text, press enter
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="10"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)

# quit
driver.quit()

