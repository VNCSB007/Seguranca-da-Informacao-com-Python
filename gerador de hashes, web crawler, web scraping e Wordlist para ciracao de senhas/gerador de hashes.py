# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 22:22:22 2021

@author: vini
"""

import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input(''' ####MENU - ESCOLHA O TIPO DE HASH ####''
             1) MD5
             2) SHA1
             3) SHA256
             4) SHA512
             Digite o número do hash a ser gerado: '''))
             
if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("\nA hash MD5 da string", string, "é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("\nA hash SHA1 da string", string, "é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("\nA hash SHA256 da string", string, "é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("\nA hash SHA512 da string", string, "é: ", resultado.hexdigest())
else:
    print ('''\nEu não sei o que fazer, jovem 
           ( ╥ ω ╥ )
           me dê um número entre 1 a 4, eu quero te mostrar uma coisa mt legal com hashs 
           ヽ(￣ω￣(°▽ ° )ゝ''')


#resultado = hashlib.md5(string.encode('utf-8'))
#é a mesma coisa que fazer: resultado = hashlib.md5(b'python security')

#print("O hash da string é: ", resultado.hexdigest())