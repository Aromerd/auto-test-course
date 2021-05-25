import time
from selenium import webdriver


def oof():
    driver = webdriver.Chrome()
    time.sleep(2)
    driver.get("http://suninjuly.github.io/cats.html")
    time.sleep(5)
    name = driver.find_element_by_css_selector(".card-img-top[name='bullet-cat']")
    name.click()
    time.sleep(5)
    driver.quit()
