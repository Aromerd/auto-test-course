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
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     btn = browser.find_element_by_css_selector("button[type='submit']")
#     btn.click()
#
#     first_window = browser.window_handles[0]
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#
#     answer = browser.find_element_by_id("answer")
#     answer.send_keys(y)
#
#     button = browser.find_element_by_css_selector("button[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
