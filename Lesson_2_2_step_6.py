# from selenium import webdriver
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     answer = browser.find_element_by_id("answer")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
#     answer.send_keys(y)
#
#     check = browser.find_element_by_id("robotCheckbox")
#     check.click()
#
#     radio = browser.find_element_by_id("robotsRule")
#     radio.click()
#
#     button = browser.find_element_by_css_selector("button[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
