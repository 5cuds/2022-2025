from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/watch?v=NB8OceGZGjA&t=158s")

input_element = driver.find_element(By.NAME, "search_query")
input_element.send_keys("Tech With Tim" + Keys.ENTER)

time.sleep(15)

driver.quit()
