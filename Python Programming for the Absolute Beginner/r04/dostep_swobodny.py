# Dostep swobodny
# Demonstruje indeksowanie znakow

import random

word = "piotrek"
print("Wartosc zmiennej word to: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")