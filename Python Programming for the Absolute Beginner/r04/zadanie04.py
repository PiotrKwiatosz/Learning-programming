# Gra w ktorej komputer wybiera losowo slowo ktore gracz musi odgadnac
# Komputer informuje ile liter ma slowo
# Gracz dostaje 5 szans na zadanie pytania czy jakas litera jest w tym slowie
# Komputer odpowiada tylko "tak" lub "nie"

import random

WORDS = ("kosmita", "tygrys", "samolot", "pies")

word = random.choice(WORDS)
chances = 5

print("Witaj! Zagramy w gre w ktorej musisz zgadnac ktore sobie wybralem z tych slow:")
print("\n\t", WORDS)
print("\nPodpowiem Ci ile ma liter, ale masz tylko 5 szans. Zaczynajmy!")

print("\nWybrane slowo ma tyle liter: ", len(word))

while chances > 0:
    letter_guess = input("Mozesz zadac pytanie czy jakas litera jest w tym slowie: ")
    chances = chances - 1
    if letter_guess in word:
        print("Tak")
    else:
        print("Nie.") 

guess = input("\nJakie to slowo?: ")

if guess.lower() == word:
    print("Tak! To to slowo! BRAWO!")
else:
    print("Ah. Nie udalo Ci sie zgadnac. Ukryte slowo to: ", word)


input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

