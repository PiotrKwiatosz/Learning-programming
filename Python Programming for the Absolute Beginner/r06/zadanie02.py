# Jaka to liczba?
#
# Komputer wybiera losowo liczbe z zakresu od 1 do 100
# Gracz probuje ja odgadnac, a komputer go informuje
# czy podana przez niego liczba jest: za duza, za mala,
# prawidlowa.

import random

def ask_number(question, low, high, step = 1):
    """Popros o podanie liczy z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high, step):
        print("Zgadnij pomiedzy", low, "a", high) # to dodane aby pomoc graczowi
        response = int(input(question))
    return response

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nMam na mysli pewna liczbe z zakresu od 1 do 100.")
print("Sprobuj ja odgadnac w jak najmniejszej liczbie prob.\n")

# ustaw wartosci poczatkowe
the_number = random.randint(1,100)
low = 1
high = 100
guess = ask_number("Ta liczba to: ", low, high)
tries = 1

# petla zgadywania
while guess != the_number:
    if guess > the_number:
        print("Za duza...")
        high = guess # gracz podal za duza, wiec zmienna 'high' sie zmienila
    else:
        print("Za mala...")
        low = guess # gracz podal za mala, wiec zmienna 'low' sie zmienila

    guess = ask_number("Ta liczba to: ", low, high)
    tries += 1

print("Odgadles! Ta liczba to:", the_number)
print("Do osiagniecia sukcesu potrzebowales tylko", tries, "prob!\n")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

