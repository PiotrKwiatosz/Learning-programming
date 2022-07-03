# Szubienica
#
# Klasyczna gra w szubienice. Komputer losowo wybiera slowo,
# a gracz probuje odgadnac jego poszczegolne litery. Jesli gracz
# nie odgadnie w pore calego slowa, maly ludzik zostaje powieszony.

# import modulow
from hashlib import new
import random

# stale
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
----------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
----------
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("KACPER", "BUBKI", "MUMIA", "BANAN", "PYTHON")

# inicjalizacja zmiennych
word = random.choice(WORDS)      # slowo do odgadniecia

so_far = "-" * len(word)        # kreska zastepuje nieodgadnieta litere

wrong = 0                       # liczba nietrafionych liter

used = []                       # litery juz uzyte w zgadywaniu

print("Witaj w grze 'Szubienica'.   Powodzenia!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystales juz nastepujace litery:\n", used)
    print("\nNa razie zagadkowe slowo wyglada tak:\n", so_far)

    guess = input("\n\nWprowadz litere: ")
    guess = guess.upper()

    while guess in used:
        print("Juz wykorzystales litere.", guess)
        guess = input("Wprowadz litere: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nTak!", guess, "znajduje sie w zagadkowym slowie!")

    # utworz nowa wersje zmiennej 'so_far', aby zawierala odgadnieta litere
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    
    else:
        print("\nNiestety,", guess, "nie wystepuje w zagadkowym slowie.")
        wrong += 1
        
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostales powieszony!")
else:
    print("\nOdgadles!")

print("\nZagadkowe slowo to", word)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


