import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('info.csv','w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Name', 'Price'])


def gethtml(url): #getting html of a page
    r = requests.get(url)
    r = r.content
    soup = BeautifulSoup(r,'lxml')
    with open('model.html', 'w') as f:
        f.write(soup.prettify())
    return soup

def gettitle(soup):
   return soup.title.text

def getheading_info(soup):
    a = soup.find('div' , class_ = "jumbotron")
    return a.h1.text , a.p.text

def gettingitems_info(soup):
    try:
        for i in soup.find_all('div', class_ = 'caption'):
            item = i.p.text
        
            price = i.h4.text

            csv_writer.writerow([item , price])
    except:
        pass
    return price




url = "https://webscraper.io/test-sites/e-commerce/allinone"


soup = gethtml(url)


print(gettitle(soup))


gettingitems_info(soup)


csv_file.close()