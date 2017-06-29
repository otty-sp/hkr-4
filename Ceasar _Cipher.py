#!/bin/python/ Ceasar Cipher/Otty Segura

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

D=[]
#txt vacio
txt=""
for i in s:
   if i.isalpha():
     if i.islower():
#seleccion de ejemplos
       txt= txt + chr(((ord(i)-97+k)%26)+97)
     else:
       txt = txt + chr(((ord(i)-65+k)%26)+65)
   else:
    txt = txt + i
print txt
# e imprime el txt
