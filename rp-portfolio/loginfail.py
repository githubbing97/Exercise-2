import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def Login_Test_FAIL():
    #driver.maximize_window()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    driver.find_element_by_name("username").send_keys("fail")
    driver.find_element_by_name("password").send_keys("failpassword")
    driver.find_element_by_xpath("//button[text()=/Log in]").click()
    assert 'Log in | Django site admin' == driver.title

    driver.close()
    
