id = ""
pw = ""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

version = 1.0

if __name__ == "__main__":

    driver = webdriver.Firefox()

    url = 'https://www.google.com'

    driver.get(url)

    driver.find_element_by_id('gb_70').click()
    elm = driver.find_element_by_name("identifier")
    elm .send_keys(id)
    elm.send_keys(Keys.ENTER)

    sleep(2)

    elm = driver.find_element_by_name("password")
    elm.send_keys(pw)
    elm.send_keys(Keys.ENTER)
