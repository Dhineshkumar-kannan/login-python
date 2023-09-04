import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("python",Keys.ENTER)
#driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
