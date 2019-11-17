#  https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
# https://www.linkedin.com/learning/using-python-for-automation/scraping-paginated-content

from bs4 import BeautifulSoup
import requests
# a basic function of website to test scrapting
def basic_web_page_scrap():
    url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    count = 1
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s )  price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1

########################################################################
## scrapting of the items and the prices for the page and all the webpages linked to it
def advance_web_page_scrap_multiple_pages():
    url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    count = 1
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print('%s )  price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1

    pages = soup.find('url', calss_='pagination')
    # safe the urls of other pages from the links
    urls = []
    links = soup.find_all('a', class_='page-link')
    for link in links:
        # check if it's linkable, take it ony if it's a string
        pageNum = int(link.text) if link.text.isdigit() else None
        if pageNum != None:
            x = link.get('href')
            urls.append(x)
    print(urls)
    count = 1
    for i in urls:
        newUrl = url + i
        response = requests.get(newUrl)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for i in items:
            itemName = i.find('h4', class_='card-title').text.strip('\n')
            itemPrice = i.find('h5').text
            print('%s )  price: %s, Item Name: %s' % (count, itemPrice, itemName))
            count = count + 1


advance_web_page_scrap_multiple_pages();