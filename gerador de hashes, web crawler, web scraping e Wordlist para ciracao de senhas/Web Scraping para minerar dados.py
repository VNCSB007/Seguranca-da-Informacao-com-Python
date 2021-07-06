# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:26:48 2021

@author: vini
"""

#Web Scraping permite coletar dados da web, uma forma de mineração que permite a extração de dados de sites da web, convertendo-os em informação estruturada para análises

from bs4 import BeautifulSoup
import requets

#No Windows, abra o prompt de comando e digite pip install beautifulsoup4
#No cmd novamente, digite "python -m pip install requests"

site = requests.get( ).content
#objeto site recebendo todo o conteudo da requisição....
soup = BeautifulSoup(site, "html.parser")
#objeto soup baixando do site o html
print(soup.prettyfy())
#transforma o html em string e o print vai exibir o html

*###apareceu todo o código html do site, como previsão de temperatura e tudo relacionado. podemos pesquisar com ctrl+f a máxima temp e trazer só aquilo. pegou o cara inteiro e fez ctrl+c

temperatura = soup.find("span", class_= "_block _margin-b-5 -gray")
print(temperatura.string)

###voltou a minima e a maxima temperatura do site climatempo

print(soup.title)
print(soup.title.string)

### veio o titulo do site

print(soup.a) #traz a ancor

print(soup.find("admin"))

###deu nada, não existe









#*resultado no terminal