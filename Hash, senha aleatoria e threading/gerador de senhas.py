# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:54:35 2021

@author: vini
"""

import random
import string

tamanho = int(input("Digite o tamanho de sua senha: "))
chars = string.ascii_letters + string.digits + 'ç!@#$&*()-=+/?' #é possível colocar senhar apenas com letra minúsculas ou maiúsculas com string.ascii_lowercase e string.ascii_uppercase
rnd = random.SystemRandom() #outra classe é tbm conhecida como os.urandom
print("".join(rnd.choice(chars) for i in range(tamanho)))
