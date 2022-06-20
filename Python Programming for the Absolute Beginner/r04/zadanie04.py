# Gra w ktorej komputer wybiera losowo slowo ktore gracz musi odgadnac
# Komputer informuje ile liter ma slowo
# Gracz dostaje 5 szans na zadanie pytania czy jakas litera jest w tym slowie
# Komputer odpowiada tylko "tak" lub "nie"

import random

WORDS = ("kosmita", "tygrys", "samolot", "pies")

word = random.choice(WORDS)

print("Witaj! Zagramy w gre w ktorej musisz zgadnac ktore sobie wybralem z tych slow:")
print("\n\t", WORDS)
print("\nPodpowiem Ci ile ma liter, ale masz tylko 5 szans. Zaczynajmy!")

print("\nWybrane slowo ma tyle liter: ", len(word))

answer = input("\nJakie to slowo?: ")

print("Mozesz zadac pytanie czy jakas litera jest w tym slowie: ")

for letter in word:
    input()
    if letter.lower() not in word:
        print("Nie")
    elif letter.lower() in word:
        print("Tak")
    else:
        answer == 5
        break

if answer == word:
    print("Tak! To to slowo! BRAWO!")     
    
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

