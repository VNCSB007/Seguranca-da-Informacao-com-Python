# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 22:20:17 2021

@author: vini
"""

"""
f = open("hosts.txt", "w")
f.write("www.google.com\n8.8.8.8\nwww.pudim.com.br\n4.4.4.4")
f.close()
#lembrar que está no diretório: usuarios/vinic
"""
import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    
    for ip in dump:
        print('verificando o ip: ', ip)
        resultado = os.system('ping -n 2 {}'.format(ip))
        print(resultado)
        print("-"*60)
        time.sleep(5)