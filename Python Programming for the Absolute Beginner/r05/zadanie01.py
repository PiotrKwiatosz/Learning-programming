# Program ktory wypisuje liste slow w przypadkowej kolejnosci.
# Powinien wypisywac wszystkie slowa bez zadnych powtorzen

import random
words = ["kacper", "justyna", "otrek", "funt", "ramena", "ciastko", "banan", "czekolada", "rower", "pyton"]

print("Slowa w losowej kolejnosci: \n")

for i in range(len(words)):
    word = random.choice(words)
    print(word)
    words.remove(word)  # jesli slowo 'word' jest juz wyswietlone - usuwa powtorke z listy


input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")