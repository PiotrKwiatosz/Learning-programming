# Rzut koscmi
# Demonstruje generowanie liczb losowych

import random

# generuj liczny losowe z zakresu 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("Wyrzuciles", die1, "oraz", die2, "i uzyskales sume", total)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")