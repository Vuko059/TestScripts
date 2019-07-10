from math import *
import getpass


#Librarys///////////Librarys///////////Librarys///////////Librarys///////////


def konsola():
    msg = ""
    while True:
        msg = input(">>>").lower()
        if msg == "delta":
            if msg == "delta":
                print('Starting...')
                delta()
            else:
                print('Something is wrong....')
        elif msg == "prz":
            if msg == "prz":
                print('Starting...')
                przekatna()
            else:
                print('Something is wrong....')
        elif msg == "help":
            print("""
    delta - start the delta program
    prz - start the przekatna program
    quit - exit the program
            """)
        elif msg == "quit":
            break
        else:
            print("this command doesn't exist")
#/////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////
def delta():
    print("Wzór na delte: delta = b*b - 4*a*c" )
    print("")
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))

    d = b*b - 4*a*c
    print("")
    print("Delta = ", d)
    print("")
    print("Miejsca zerowe:")
    print("")
    if d>0:
        print('x1= ', (-b - sqrt(d))/2*a)
        print('x2= ', (-b + sqrt(d))/2*a)
    if d==0:
        print('x=', -b/2*a)
    if d<0:
        print('brak pierwiastków! ')

#/////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////
def przekatna():
    print("")
    print("Przekątna wzór: ")
    print("")
    print("a pierwiastek z 2 - kwadrat")
    print("")
    print("a pierwiastek z 3 - sześcian")
    print("")
    a = int(input("Podaj krawędź a:" ))
    if a>0:
        print("Przekątna kwadratu")
        print("")
        print(a, "pierwiastek z 2",'<======>', a + sqrt(2))
        print("Przekatna szećianu")
        print("")
        print(a, "pierwiastek z 3", '<======>', a + sqrt(3))
    else:
        print('Something is wrong....')


#/////////////////////////////////////////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////

password = getpass.getpass()
if password == 'asd':
    konsola()
else:
    print('Worng password...')
