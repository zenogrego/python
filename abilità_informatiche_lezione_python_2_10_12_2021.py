#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:04:24 2021

@author: zenogregorin
"""

############# PACCHETTI #############

import math


#####################################



a=3
print(type(a)) #sulla console mi dice che è un int

b = 12.345
print(type(b)) #sulla console mi dice che è un float

r = 12 + 5j
print(type(r)) #sulla console mi dice che è un complex

k = 5 
s = 5 + 1j
print(type(s+k)) #sulla console mi dice che è un complex
 

math.pi
print(math.pi) #printiamo il valore di pigreo sulla console

math.e
print(math.e) #printiamo il valore di e sulla console

math.sin(2)
print(math.sin(2)) #printiamo il seno di 2 

#definiamo area del cerchio 

r = 14 #imposto un raggio pari a 14 

area = math.pi * r**2 #definiamo l'area del cerchio 

print(area) #in console faccio plottare il risultato 

var1 = 'hello world!'
var2 = "python programming"

print("var1[0]:", var1[0])   #in console mi printa la prima lettera di var1, cioè 0 
print("var2[1:5]:", var2[1:5])  #in console mi printa le prime 4 lettere di var2, cioè ython




########### string type operators ###########

a = 'Hello'

b=a+a+a    #concatenazione 

print(b)


c = 'He'+'l'*2+'o World'   #concatenazione multipla

print(c)



nome = "Zeno"
my_string = " Ciao %s" % nome
my_string = " Ciao %s, come stai? %s" % (nome, 'tutto ok zio')
print(my_string)


##########  row string ##########


w = r'Hello \t World'  #raw string

print(w)

  
