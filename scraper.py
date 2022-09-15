import requests
from bs4 import BeautifulSoup

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html.parser')  # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())