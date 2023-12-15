# Write a Python program to print the element(s) that has a specified id of a given web page.

from bs4 import BeautifulSoup
import requests

URL = 'https://python.org'
ID='#back-to-top-1'

if __name__=='__main__':
     response = requests.get(URL)
     bs_python_org=BeautifulSoup(response.content,'html.parser')
     tag_with_ID=bs_python_org.select_one(ID)

     for child_content in tag_with_ID:
          print(child_content)
