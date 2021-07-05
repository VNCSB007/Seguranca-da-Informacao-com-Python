# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 16:47:04 2021

@author: vini
"""

import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso!")
    
    HostAlvo = input("Digite o Host ou IP a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")
    
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("-"*60)
        print("Cliente TCP conectado com Sucesso no Host: {}, na Porta {}".format(HostAlvo, PortaAlvo))
        print("-"*60)
        s.shutdown(2)
    
    except socket.error as e:
        print("-"*60)
        print("\nA conexão falhou... Não foi possível conectar no Host {}, na Porta {} :(".format(HostAlvo, PortaAlvo))
        print("erro: " + str(e))
        print("-"*60)
        sys.exit()
    
if __name__ == "__main__":
    main()
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        