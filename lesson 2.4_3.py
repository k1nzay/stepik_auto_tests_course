from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100'))
    browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()


finally:
    time.sleep(10)
    browser.quit()