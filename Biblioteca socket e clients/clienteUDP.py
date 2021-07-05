# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:37:45 2021

@author: vini
"""


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")
print("-"*60)

host = "localhost"
porta = 5432

s.bind((host, porta))
mensagem = "Servidor: Oláááá cliente eae suave?"

while 1:
    dados, endereco = s.recvfrom(4096)
    if dados:
        print("Servidor enviando mensagem...")
        s.sendto(dados + mensagem.encode()code(()), end)



"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")
print("-"*60)

host = "localhost"
porta = 5432
mensagem = "olá servidor, suabile?"

try: 
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print("Cliente: fechando a conexão")
    s.close()
"""