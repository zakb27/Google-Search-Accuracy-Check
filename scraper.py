import requests
import re
from bs4 import BeautifulSoup

URL = "https://finmead.weebly.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html.parser')  # If this line causes an error, run 'pip install html5lib' or install html5lib
all_text = soup.get_text(strip=True, separator=u' ')
all_text = re.sub('\\s', ' ', all_text)
all_text = re.sub('[0-9]', ' ', all_text)
all_text = re.sub('[ ]{2,}', ' ', all_text)

print(all_text)