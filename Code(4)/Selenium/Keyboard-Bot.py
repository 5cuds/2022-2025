import pyautogui as auto
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.monkey-type.org")
driver.implicitly_wait(15)


parent_span = driver.find_element(By.XPATH, "//span[@class='active']")
child_spans = driver.find_elements(By.XPATH, "//span[@class='active']//span")

for text in child_spans:
    print(f"Letter: {text.text}")
    print("dadasd")

time.sleep(145)
driver.quit()
