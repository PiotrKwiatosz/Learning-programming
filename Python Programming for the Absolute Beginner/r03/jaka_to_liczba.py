# Jaka to liczba?
#
# Komputer wybiera losowo liczbe z zakresu od 1 do 100
# Gracz probuje ja odgadnac, a komputer go informuje
# czy podana przez niego liczba jest: za duza, za mala,
# prawidlowa.

import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na mysli pewna liczbe z zakresu od 1 do 100.")
print("Sprobuj ja odgadnac w jak najmniejszej liczbie prob.\n")

# ustaw wartosci poczatkowe
the_number = random.randint(1,100)
guess = int(input("Ta liczba to: "))
tries = 1

# petla zgadywania
while guess != the_number:
    if guess > the_number:
        print("Za duza...")
    else:
        print("Za mala...")

    guess = int(input("Ta liczba to: "))
    tries += 1

print("Odgadles! Ta liczba to:", the_number)
print("Do osiagniecia sukcesu potrzebowales tylko", tries, "prob!\n")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")