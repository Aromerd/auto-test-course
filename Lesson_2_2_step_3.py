# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time
#
#
# def calc(x, y):
#     ans = x + y
#     return ans
#
#
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element_by_id("num1").text
#     x = int(x)
#     y = browser.find_element_by_id("num2").text
#     y = int(y)
#     z = calc(x, y)
#     z = str(z)
#
#     select = Select(browser.find_element_by_id("dropdown"))
#     select.select_by_value(z)
#
#     button = browser.find_element_by_css_selector("button[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(3)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
