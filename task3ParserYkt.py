import requests
from bs4 import BeautifulSoup

url = 'https://rabota.ykt.ru/jobs?categoriesIds=2083'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36', 'accept':'*/*'}
r = requests.get(url, headers=header, params=None)

soup = BeautifulSoup(r.text, features="html.parser")
vacanies=soup.find_all('span', {'class': 'r-vacancy_title'})
for vacancy in vacanies:
  print(str(vacancy).split('</')[0].split('>')[1])