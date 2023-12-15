# Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from .

from bs4 import BeautifulSoup
import requests

URL = 'https://python.org'

def get_link_within_a_tag(document:BeautifulSoup,tag:str())-> list[str()]:
     return [children_tag.find('a')['href'] for children_tag in document.find_all(tag)]

if __name__=='__main__':
     response = requests.get(URL)
     bs_python_org=BeautifulSoup(response.content,'html.parser')
     page_urls=get_link_within_a_tag(bs_python_org,'li')

     for url in page_urls:
          print(url,end='\n\n')