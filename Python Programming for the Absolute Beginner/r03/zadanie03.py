# Zmodyfikowany program 'Jaka to liczba' tak, aby gracz dysponowal ograniczona 
# liczba prob odgadniecia wybranej przez komputer liczby.
# Gdy graczowi nie uda sie odgadnac tej liczby w wyznaczonej liczbie prob, program powinien wyswietlic
# odpowiedni komunikat z reprymenda.

import random

print("\tWitaj w grze 'Jaka to liczba'! wersja HARDCORE!")
print("\nMam na mysli pewna liczbe z zakresu od 1 do 100.")
print("Sprobuj ja odgadnac w jak najmniejszej liczbie prob.\n")
print("Masz na to tylko 10 prob!\n")

# ustaw wartosci poczatkowe
the_number = random.randint(1,100)
guess = int(input("Ta liczba to: "))
tries = 10

# petla zgadywania
while tries > 0:
    if guess > the_number:
        print("Za duza...")
    elif guess < the_number:
        print("Za mala...")
    
    elif guess == the_number:
        print("\nOdgadles! Ta liczba to: ->", the_number)
        print("Do osiagniecia sukcesu potrzebowales tylko", 10 - tries , "z 10 prob!\n")
        break

    else:
        print("Niemozliwa liczba")

    guess = int(input("Ta liczba to: "))
    tries -= 1

if tries == 0:
    print("\nKONIEC! Nie udalo Ci sie zgadnac w 10 probach...")
    print("\nUciekla i nie zlapale jej...")
    print("\n\tA byla to: ->", the_number, "<- liczba...")
    print("\nPostaraj sie bardziej!!!")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")