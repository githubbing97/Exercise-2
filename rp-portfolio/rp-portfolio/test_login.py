from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()

    
def test_ablelogin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    user = driver.find_element_by_name("username")
    user.clear()
    user.send_keys("malcolm")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("@ministration")
    password.send_keys(Keys.RETURN)
    assert 'Site administration | Django site admin' in driver.title

def test_unablelogin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    user = driver.find_element_by_name("username")
    user.clear()
    user.send_keys("mal")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("@ministration")
    password.send_keys(Keys.RETURN)
    assert 'Log in | Django site admin' in driver.title
    
