from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome(r'C:\chromedriver\chromedriver.exe')
    browser.get(link)

    # Waiting for low price
    WebDriverWait(browser,14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_tag_name('button').click()

    # Alert window
    # confirm = browser.switch_to.alert
    # confirm.accept()

    # New window
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value")
    answer = calc(x.text)
    print(answer)
    browser.find_element_by_tag_name('input').send_keys(answer)
    browser.find_element_by_id("solve").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
