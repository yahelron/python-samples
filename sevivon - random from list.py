import random
import time
import sys
from selenium import webdriver
sevivon = ['פ','נ','ג','ה']

matil = random.choices(sevivon)
print("ברוך הבא למשחק הסביבון שלנו. אתה עומד להטיל סביבון")
any_key = input('לחץ על c כדי להמשיך ')
if any_key == 'c':
    print("מסובב עכשיו...") ;
    time.sleep(2)
else:
    sys.exit()


print(matil)
if matil == ['פ']:
    print("הפסדת! שלם לקופה ")
elif matil == ['ג']:
    print('הרווחת את כל הקופה')
    ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                                 executable_path='geckodriver.exe')
    ffdriver.get("https://www.youtube.com/")
    ffdriver.find_element_by_name("search_query").send_keys("we are the champions")
    ffdriver.find_element_by_id("search-icon-legacy").click()
    ffdriver.find_element_by_id("video-title").click()
elif matil == ['נ'] :
    print('לא הרווחת ולא הפסדת')
elif matil ==['ה'] :
    print('הרווחת חצי מהקופה')

