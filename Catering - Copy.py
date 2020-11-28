'''
    Name: Mellvin Soriano
    Class: CIS 108 M02
    Instructor: A. Atshan
    Program Name: Catering.py
    Description: The Passaic County Catering and Convention Services modified the requirements for their billing program.
    Write a Python program to produce the customers’ bills.  
'''

#import goes here
import math
from random import randint

#constants go here
tax=0.06875
hallA=1000.00
hallB=850.00
hallC=750.00
hallH=0.00
standard=21.75
deluxe=25.95
gratuity=0.2
invoice=randint(100,999)
discount=0.00

def main():
    #   Output Section
    pcccsBill()
    pcccsFinalBill()

def pcccsBill():
    #   Input Section
    global adults
    adults=int(input("Number of adults attending: "))
    global children
    children=int(input("Number of children attending: "))
    print("\tAdult Meal\n\t1 - Standard meal $21.75\n\t2 - Deluxe meal $25.95")
    global meal
    meal=int(input("Number: "))    
    print("\tHall Menu\n\t1 - Hall A\n\t2 - Hall B\n\t3 - Hall C\n\t4 - Hall H (Catering to home)")
    global hall
    hall=int(input("Number: "))
    global weekend
    weekend=input("Weekend Catering (Y (Yes) or N (No)): ")
    global speedy
    speedy=input("Speedy Payment (Y (Yes) or N (No)): ")
    global deposit
    deposit=float(input("Deposit: "))

    #   Processing Section
    response=['Y','no','Yes','N','No','yes']

def adultchildMeal(meal):
    if meal==1:
        txtmeal=print('{:>45}'.format('Cost per standard meal for adult:\t$')+str(standard))
        txtchildmeal=print('{:>45}'.format('Cost per standard meal for child:\t$')+format(standard/2,".2f")
    elif meal==2:
        txtmeal=print('{:>45}'.format("Cost per deluxe meal for adult:\t$")+str(deluxe))
        txtchildmeal=print('{:>45}'.format('Cost per deluxe meal for child:\t$'),format(deluxe/2,".2f")
    return txtmeal, txtchildmeal
    
    

def pcccsFinalBill():
    header= '/-'
    subheader='-'
    print("\n",header[:2]*31+"/")
    print(format("Caswell Catering and Convention Services",">45s"))
    print('{:>35}'.format('Final Bill'),'{:>20}'.format('Invoice#'),invoice)
    print(header[:2]*31+"/")
    print('{:>45}'.format('Number of adult:\t'),adults)
    print('{:>45}'.format('Number of children:\t'),children)
    print('{:>45}'.format('Gratuity:\t'),int(gratuity*100),'%')
    #print('{:>45}'.format('Weekend:\t'),weekend)
    adultCost,childCost=adultchildMeal(meal)
    print(subheader[:1]*64)
    
    
    print(header[:2]*31+"/") #End
    print('{:>45}'.format('Thank you for using Caswell Catering'))

for nextone in range(1):
    main()
input("\n\nPress Enter to Continue")
