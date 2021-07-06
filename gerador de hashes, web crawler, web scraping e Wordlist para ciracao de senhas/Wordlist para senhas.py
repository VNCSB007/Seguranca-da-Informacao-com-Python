# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:06:39 2021

@author: vini
"""

#Wordlists é um arquivo contendo uma palavra por linha. é uma forma de atacar agressivamente a segurança de um sistema. serve para testar autenticação e confidencialidade

import itertools

string = ('abcd')

resultado = itertools.permutations(string, len(string)) #lembrando que o numero de permutações não pode ser maior que o número de caracteres da string

for i in resultado:
    print(''.join(i))