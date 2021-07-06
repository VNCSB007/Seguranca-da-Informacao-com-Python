# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:12:40 2021

@author: vini
"""

import re
import json
from urllib.request import urlopen



url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo:\n')
print(f'IP: {ip}\nRegião: {regiao}\nPaís: {pais}\nCidade: {cidade}\nOrganização: {org}')












