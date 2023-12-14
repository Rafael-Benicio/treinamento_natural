# Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from .

from bs4 import BeautifulSoup
import requests

URL = 'https://python.org'

if __name__=='__main__':
     response = requests.get(URL)
     bs_python_org=BeautifulSoup(response.content,'html.parser')
     page_urls=[i.find('a')['href'] for i in bs_python_org.find_all('li')]
     for url in page_urls:
          print(url)