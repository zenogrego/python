#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:00:40 2021

@author: zenogregorin
"""

one = 1 
two = 2 

three= one + two 

print (three) 


hello = "hello"
world = "world"

helloworld = hello + world

print (helloworld)

A = 2

x = 4

def func(x, A):
    return A * x**2

print (func(x, A))

def print_user_info(name, age = 26):
    print ("Name", name) 
    print ("Age", age ) 
    
print_user_info(age = 26, name = "Zeno")
print_user_info(name = "Zeno")

total = 0
def sum(arg1, arg2):
    total = arg1 + arg2 
    print("inside the function local total:", total)
    return total 
    
total = sum(10,20)
print(" outside the functionglobal local:", total)

def changelist(mylist):
    mylist=[1,2,3]
    print("values inside the function:", mylist)
    return mylist

list=[10,20,30]
mylist=changelist(list)
print("values after the function:", mylist)