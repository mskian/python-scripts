#!/usr/bin/env python

from __future__ import division

print("\n***********[CUT OFF CALCULATOR]***********\n")

## Cut off Choice
def menu():
    print("-------------------WELCOME-------------------")
    print("1. Cut Off Calculator - Engineering")
    print("2. Cut Off Calculator - Medical")
    print("3. Cut Off Calculator - Pure Science(Medical)")
    print("4. Cut Off Calculator - Agriculture")
    print("5. Exit")
    print("-------------------*******-------------------")

## User Input
menu()
CHOICE = input("\n\033[1;91mENTER YOUR CHOICE: \033[1;m")

# Cut Off Calculator - Engineering
if CHOICE == '1':
    try:

        A = int(input('\033[1;32mEnter a Maths Mark = \033[1;m'))
        B = int(input('\033[1;32mEnter a Physcis Mark = \033[1;m'))
        C = int(input('\033[1;32mEnter a Chemistry Mark = \033[1;m'))

        ## CalCulate Cut off
        D = (A/2 + B/4 + C/4)

    except (SyntaxError, ValueError):

        print("Empty Input or Wrong Input Value")

    else:

        print('\033[1;33mYOUR CUT OFF MARK IS = %s \033[1;m' %D)

## Cut Off Calculator - Medical
elif CHOICE == '2':

    try:

        A = int(input('\033[1;32mEnter your Biology Mark = \033[1;m'))
        B = int(input('\033[1;32mEnter your Physics Mark = \033[1;m'))
        C = int(input('\033[1;32mEnter your Chemistry Mark = \033[1;m'))

        ## CalCulate Cut off
        D = (A/2 + B/4 + C/4)

    except (SyntaxError, ValueError): ## Python3X

        print("Empty Input or Wrong Input Value")

    else:

        print('\033[1;33mYOUR CUT OFF MARK IS = %s \033[1;m' %D)

## Cut Off Calculator - Pure Science(Medical)
elif CHOICE == '3':

    try:

        A = int(input('\033[1;32mEnter your Botany Mark = \033[1;m'))
        B = int(input('\033[1;32mEnter your Zoology Mark = \033[1;m'))
        C = int(input('\033[1;32mEnter your Physics Mark = \033[1;m'))
        D = int(input('\033[1;32mEnter your Chemistry Mark = \033[1;m'))

        ## CalCulate Cut off
        E = (A/4 + B/4 + C/4 + D/4)

    except (SyntaxError, ValueError): ## Python3X

        print("Empty Input or Wrong Input Value")

    else:

        print('\033[1;33mYOUR CUT OFF MARK IS = %s \033[1;m' %E)

## Cut Off Calculator - Agriculture
elif CHOICE == '4':

    try:

        A = int(input('\033[1;32mEnter your Biology Mark = \033[1;m'))
        B = int(input('\033[1;32mEnter your Maths Mark = \033[1;m'))
        C = int(input('\033[1;32mEnter your Physics Mark = \033[1;m'))
        D = int(input('\033[1;32mEnter your Chemistry Mark = \033[1;m'))

        ## CalCulate Cut off
        E = (A/4 + B/4 + C/4 + D/4)

    except (SyntaxError, ValueError): ## Python3X

        print("Empty Input or Wrong Input Value")

    else:

        print('\033[1;33mYOUR CUT OFF MARK IS = %s \033[1;m' %E)

elif CHOICE == '5':
    print('Exiting')

else:
    print('\033[1;31m [-] Invalid option! \033[1;m')
