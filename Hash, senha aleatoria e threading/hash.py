# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:09:15 2021

@author: vini
"""

#importante ir para python.org para verificar a documentação completa do Python

import hashlib


hash1 = hashlib.new('ripemd160')
hash1.update(open("C:/Users/vinic/OneDrive/Desktop/Trabalhos/Trabalhos do Curso Online/DIO/arquivos Python/Segurança da informação/Novo projeto/a.md", 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open("C:/Users/vinic/OneDrive/Desktop/Trabalhos/Trabalhos do Curso Online/DIO/arquivos Python/Segurança da informação/Novo projeto/b.md", 'rb').read())
    
if hash1.digest() != hash2.digest():
    print("diferentes!")
else:
    print("iguais!")
    
    
    
    
    
    
    
    
    
    
    