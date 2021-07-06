# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:23:49 2021

@author: vini
"""

import phonenumbers
from phonenumbers import geocoder

phone = input("digite o telefone no formato +551145645645")

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

#o print resulta na região do mundo em que o número está ligando