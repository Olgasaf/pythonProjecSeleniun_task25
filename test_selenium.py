#pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe
import pytest
import time
def test_show_my_pets(show_my_pets):
   # проверяем, что у меня есть питомцы
   list_pets = pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')
   for i in range(len(list_pets)):
      assert list_pets[i].get_attribute('src') != ''

#Присутствуют все питомцы
def test_all_my_pets(show_my_pets):
   list_pets = pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')

   pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

   # количество питомцев по списку
   number = list_pets[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   #количество карточек питомцев
   number_of_pets = len(pets)

   # Проверяем что количество питомцев по списку совпадает с количеством карточек питомцев
   assert number == number_of_pets
#У питомцев есть фото, возраст и вид
def test_all_pets(show_my_pets):
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-tex')
   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

#Хотя бы у половины питомцев есть фото

def test_photo_all_my_pets(show_my_pets):
   # количество питомцев по списку
   statistic= pytest.driver.find_elements_by_css_selector('.\\.col-sm-4.left')
    
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   print(f'\n Всего питомцев: {number}')

   #половина питомцев
   number_haif = number // 2

   
   #количество питомцев с фото
   pets_photo = pytest.driver.find_elements_by_css_selector('.table.table-hover img')
   pets_all_photo = 0
   for i in range(len(pets_photo)):
      if pets_photo[i].get_attribute('src') != '':
         pets_all_photo += 1
   print(f'\n питомцев с фото: {pets_all_photo}')
#Проверяем, что хотя бы у половины питомцев есть фото
   assert pets_all_photo >= number_haif













