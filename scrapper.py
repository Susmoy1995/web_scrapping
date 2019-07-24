# web scrapping file
from bs4 import BeautifulSoup
import requests

with open('Documents/sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

for article in soup.find_all('article'):
    print(article.h2.text)
