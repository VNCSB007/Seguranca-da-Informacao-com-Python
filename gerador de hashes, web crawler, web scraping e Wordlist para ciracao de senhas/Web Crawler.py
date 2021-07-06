# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 01:06:04 2021

@author: vini
"""

#tem nomes como spider e robot. cadastra as informações que tem nos IPs e traz o que tem de mais relevante (palavras ~ chaves)

from bs4 import BeautifulSoup
import requests
import operator 
from collections import Counter


def start(url):  #define todo o web crawler
    
    worldlist = []
    source_code = requests.get(url).text
    
    soup = BeautifulSoup(source_code, "html.parser")
    
    for each_text in soup.findAll ('div', {'class': 'entry-content'}):
        content = each_text.text
        
        words = content.lower().split
        
        for each_word in words:
            worldlist.append(each_word)
        clean_worldlist(worldlist)
        
        
        
def clean_worldlist(worldlist):
    clean_list = []
    for word in worldlist:
        symbols = '!@#$%&*()_-=+{[}]|\;:"<>?/., '
        
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
            
        if len(word) > 0:
            clean_list.append(word)
    
    
    create_dictionary(clean_list)
   
    
   
def create_dictionary (clean_list):
    word_count = {} 
    
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
            
            
            
    for key, value in sorted(word_count.items(), key_=_opearator.itemgetter(1)):
        print("% s : % s " % (key, value))
        
    c = Counter(word_count)
        
    top = c.most_commom(10)
    print(top)
    
if __name__ == "__main__":
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")
        
    
            
        
        
    
    








