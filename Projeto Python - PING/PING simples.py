 # -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 21:40:30 2021

@author: vini
"""

import os #importa o módulo ou biblioteca 'os' (integra os programas e recursos do S.O.)

print("#"* 60) ## imprimindo o sharp, sustenido ou cerquilha em 60 vezes para dar a divisão (de agora em diante, ele será chamado de "separador")

ip_ou_host = input("digite o IP ou Host a ser verificado: ")
#criamos uma variável que receberá, do usuário, um IP

print("\nO IP ou Host dado foi: {}".format(ip_ou_host)) #verificando o IP dado
print("-" *60) #separador

resposta = os.system('ping -n 4 {}'.format(ip_ou_host)) #chamando sistema da biblioteca os - comando ping
print(resposta)
print("-" *60) #separador
