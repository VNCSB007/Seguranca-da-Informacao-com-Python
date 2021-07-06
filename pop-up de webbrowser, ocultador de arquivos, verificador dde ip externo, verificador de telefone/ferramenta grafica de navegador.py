# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:25:54 2021

@author: vini
"""

import webbrowser
from tkinter import *


root = Tk( )
root.title('Abrir Browser')
root.geometry('200x100') #ele colocou 300x200


def google():
    webbrowser.open('www.google.com')
    
mygoogle = Button(root, text = "Abrir o Google", command = google).pack(pady = 20)

root.mainloop()