import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.boursorama.com/bourse/devises/taux-de-change/"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')

div = soup.find('div', class_="u-relative")
table = div.find('table')

headers = []
thead = table.find('thead')
if thead:
    headers = [th.text.strip() for th in thead.find_all('th')] 

rows = []
tbody = table.find('tbody')
for tr in tbody.find_all('tr'):
    cells = tr.find_all(['td', 'th'])
    row = [cell.text.strip() for cell in cells]
    rows.append(row)

data = pd.DataFrame(rows, columns=headers)
print(data.head())
data.to_excel('table.xlsx', index=False)