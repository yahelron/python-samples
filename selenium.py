import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
### 1.  Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox

ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
chromdriver = webdriver.Chrome(executable_path="e:/devops/Class3/chromedriver.exe")
chromdriver.get("http://www.walla.co.il")
ffdriver.get("http://www.ynet.co.il")
# 2. In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you
# created in clause 1.
#  למה הכוונה website name?
# url?
website_title = ffdriver.title
print(website_title)
#ffdriver.refresh()
website_name = 'mywebsite'
print(weburl)
if website_title == website_name:
    print("The same")
ffdriver.quit()
"""""""""
# 3. Open a few browsers, locate any element, does the
# element has the same locators in the other browser?
# answer: yes, they are the same.

# 4. Create a test with the following:
#  Open Google Translate web page
#  Write anything in Hebrew in the text area
את רוב התשובות בדקתי עם ויירפוקס בגלל בעייה עם התקנת הכרום.
"""""""""
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("https://translate.google.co.il/?hl=iw#view=home&op=translate&sl=iw&tl=en")
ffdriver.find_element_by_id("source").send_keys("איך קוראים לך")
ffdriver.quit()

# 5
# Open Youtube web page
# Type a name of a song
# Click on search.
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("https://www.youtube.com/")
ffdriver.find_element_by_name("search_query").send_keys("Leonard cohen everybody knows")
ffdriver.find_element_by_id("search-icon-legacy").click()
ffdriver.find_element_by_id("video-title").click()
ffdriver.quit()

# 6. Open Chrome browser on Google Translate website:
# https://translate.google.com/
#  Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement
# you created.
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("https://translate.google.com/")
a = ffdriver.find_element_by_id("source")
b = ffdriver.find_element_by_class_name("orig")
c = ffdriver.find_element_by_name("source-header")
#c = ffdriver.find_element_by_xpath("//input[@autocapitalize=‘off']")
print("a =",a,"b = ",b , "c = ", c)
ffdriver.quit()
# 7.
# Open Chrome browser on Facebook website
# https://www.facebook.com/
# Login into Facebook (No need to send me credentials).
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("https://www.facebook.com//")
ffdriver.find_element_by_id("pass").send_keys("mypass...")
ffdriver.find_element_by_id("email").send_keys("myemail@gmail.com")
ffdriver.find_element_by_id("loginbutton").click()
ffdriver.quit()


8.
# Open Chrome browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.delete_all_cookies()
print(ffdriver.get_cookies())
ffdriver.quit()
#9.
# Open any browser on "Github" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).

ffdriver = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe",  executable_path='geckodriver.exe')
ffdriver.get("http://www.github.com")
input_element = ffdriver.find_element_by_name("q")
input_element.send_keys("selenium")
input_element.submit()
ffdriver.quit()
