import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://phonesdata.com/pt/smartphones/apple/iphone-16e-5465147/')

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todos_dados = dados_pagina.find_all('div', class_="product-page-content")

print(todos_dados)
 