from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# # Открытие сайта
# driver.get("https://itcareerhub.de/ru")
# # Задержка перед закрытием браузера
# sleep(50)

service = Service("/Users/st/Downloads/chromedriver-mac-arm64/chromedriver")
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://itcareerhub.de/ru")
sleep(2)
# driver.refresh()
# sleep(2)
# driver.set_window_size(640, 460)
# sleep(2)
# driver.get("https://www.berlin.de")
# # driver.save_screenshot("./berlin_screenshot.png")
# driver.back()
# # Задержка перед закрытием браузера
# sleep(10)
 # Поиск ссылки "О нас" и клик
about_link = driver.find_element(By.LINK_TEXT, "О нас")
about_link.click()
# Задержка для проверки перехода
sleep(5)
# driver.quit()

# driver.save_screenshot("путь_к_файлу")
# driver.save_screenshot("./berlin_screenshot.png")

# import os
# print(os.getcwd()