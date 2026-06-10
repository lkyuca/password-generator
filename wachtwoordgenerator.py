print ("welcome gebruiker")
import random
tekens  = ("abcdefghijklmnopqurstvxyzABCDEFGHIJKLMNOPQURSTVXYZ1234567890!@#$%^&*")
hoeveel =int(input("hoeveel wachtwoorden wil jij ?  :"))
lengte = int(input("hoeveel lang moet uw wachtwoord zijn :"))
for x in range (hoeveel):
    wachtwoord = ' '
    for x in range (lengte) :
                    wachtwoord += random.choice(tekens)
    print (wachtwoord)
