# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:00:06 2021

@author: vini
"""


import ctypes

pasta = input("digite a pasta a ser ocultada(e.g. C:/pasta): ")

atributos_ocultar = 0x02 #atributo hexadecimal de ocultar arquivos

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributos_ocultar)

if retorno:
    print('\narquivo foi ocultado!')
else:
    print('\nnão deu irmão...')
