# -*- coding: utf-8 -*-

'''
Created on 27 nov. 2020

@author: danie
'''
from crime import*
if __name__ == '__main__':
    crime=leer_crimenes('../data/Crime_Data_Usa.csv')
    print(crime[:3])