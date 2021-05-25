# from selenium import webdriver
# import time
# import os
#
#
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     first_name = browser.find_element_by_css_selector("input[name='firstname']")
#     first_name.send_keys("Ivan")
#     last_name = browser.find_element_by_css_selector("input[name='lastname']")
#     last_name.send_keys("Petrov")
#     email = browser.find_element_by_css_selector("input[name='email']")
#     email.send_keys("ivanpetrov@mail.ru")
#
#     # нашли текущую директорию питон файла
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     # добавили к ней имя файла
#     file_path = os.path.join(current_dir, "test.txt")
#     # нашли кнопку загрузки файла
#     biography = browser.find_element_by_id("file")
#     # прямо в эту кнопку вставили путь к файлу
#     biography.send_keys(file_path)
#
#     button = browser.find_element_by_css_selector("button[type='submit']")
#     button.click()
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
