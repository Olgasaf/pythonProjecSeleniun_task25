import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture
def show_my_pets():
   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))

   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('OlgaSafy@yandex.ru')

   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('andrey160894')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   """Нажимаем на ссылку "Мои питомцы" """
   pytest.driver.find_element_by_link_text("Мои питомцы").click()

   # Устанавливаем неявное ожидание
   myDynamicElement = pytest.driver.find_element_by_id("all_my_pets")

