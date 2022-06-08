# Wymieszane litery
# Komputer wybiera losowo slowo a potem miesza w nim litery
# Gracz powinien odgadnac pierwotne slowo

from calendar import c
import random

# utworz sekwencje slow do wyboru
WORDS = ("python", "anagram", "piotrek", "trudny", "pomieszany", "odpowiedz")

# wybierz losowo jedno slowo z sekwencji
word = random.choice(WORDS)

# utworz zmienna, by pozniej uzyc jej do sprawdzenia, czy odpowiedz jest poprawna
correct = word

# utworz 'pomieszana' wersje slowa
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# rozpocznij gre
print(
"""
        Witaj w grze 'Wymieszane litery'!
        
    Uporzadkuj litery, aby odtworzyc prawidlowe slowo.
(Aby zakonczyc zgadywanie, nacisnij klawisz Enter bez podawania odpowiedzi.)"""
)
print("Zgadnij, jakie to slowo:", jumble)

guess = input("\nTwoja odpowiedz: ")
while guess != correct and guess != "":
    print("Niestety, to nie to slowo.")
    guess = input("Twoja odpowiedz: ")

if guess == correct:
    print("Zgadza sie! Zgadles!\n")

print("Dziekuje za udzial w grze.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")