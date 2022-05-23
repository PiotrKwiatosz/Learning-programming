# Program ktory 'rzuca' 100 razy moneta,
# a nastepnie podaje uzytkownikowi liczbe orzelkow i reszek

import random

throws = int(100)
orzelki = random.randint(1, 100)
reszki = throws - orzelki

print("Wyrzuciles", orzelki, "orzelkow, i", reszki, "reszek")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


