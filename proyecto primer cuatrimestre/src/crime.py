# -*- coding: utf-8 -*-

'''
Created on 27 nov. 2020

@author: danie
'''
import csv
from collections import namedtuple
from datetime import date

crime = namedtuple('crime','State, City, Year, Population, Violent_Crime, Murder, Rape, Robbery, Aggravated_assault, Property_Crime, Burglary, Larceny_Theft, Motor_Vehicle_Theft, Arson')

def leer_crimenes(fichero):
    
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        
        for State,City,Year,Population,Violent_Crime,Murder,Rape,Robbery,Aggravated_assault,Property_Crime,Burglary,Larceny_Theft,Motor_Vehicle_Theft,Arson in lector:
            if State=="":
                State='ALABAMA'
            if City=="":
                City='GILBERT'
            if Year=="":
                Year='2020'
            if Population=="":
                Population='456'
            if Violent_Crime=="":
                Violent_Crime='456'
            if Murder=="":
                Murder='100'
            if Rape=="":
                Rape='234'
            if Robbery=="":
                Robbery='457'
            if Aggravated_assault=="":
                Aggravated_assault='78'
            if Property_Crime=="":
                Property_Crime='2345'
            if Burglary=="":
                Burglary='345'
            if Larceny_Theft=="":
                Larceny_Theft='4561'
            if Motor_Vehicle_Theft=="":
                Motor_Vehicle_Theft='127'
            if Arson=="":
                Arson='34'    
            q=crime(str(State),str(City),float(Year),int(Population),int(Violent_Crime), int(Murder), int(Rape), int(Robbery), int(Aggravated_assault), int(Property_Crime), int(Burglary), int(Larceny_Theft), int(Motor_Vehicle_Theft), int(Arson))
            registros.append(q)
            
           
    return registros
            

                
 
    
