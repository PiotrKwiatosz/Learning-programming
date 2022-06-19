# POPRAWIONE Wymieszane litery
# Komputer wybiera losowo slowo a potem miesza w nim litery
# Gracz powinien odgadnac pierwotne slowo

# Gracz ma teraz mozliwosc zobaczenia podpowiedzi
# Dodany system punktacji

from calendar import c
import random

# utworz sekwencje slow do wyboru
WORDS = ("python", "anagram", "piotrek", "trudny", "pomieszany", "odpowiedz")

# podpowiedzi do slow
hint1 = ("Jezyk programowania ktory jest na litere P",  "python")
hint2 = ("Gram i ana-nas, jak to mozna zlaczyc?", "anagram")
hint3 = ("Male zdrobnienie do imienia wielkiego Apostola", "piotrek")
hint4 = ("Jak nielatwy to jaki?", "trudny")
hint5 = ("Jak cos sie miesza to jakie sie staje? I jaki ktos moze byc?", "pomieszany")
hint6 = ("Pytanie i ...?", "odpowiedz")

HINTS = (hint1, hint2, hint3, hint4, hint5, hint6)

answer = ("tak" or "nie")

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
        Witaj w grze 'Wymieszane litery'! v. 2.0 z Zadania 3
        
    Uporzadkuj litery, aby odtworzyc prawidlowe slowo.
(Aby zakonczyc zgadywanie, nacisnij klawisz Enter bez podawania odpowiedzi.)

    !! W tej wersji dostepne sa juz podpowiedzi jesli utkniesz w martwym punkcie
    oraz system punktacji po zakonczeniu rozgrywki (najwiecej punktow bez podpowiedz) !!"""
)
print("Zgadnij, jakie to slowo:", jumble)

guess = input("\nTwoja odpowiedz: ")
while guess != correct and guess != "":
    print("Niestety, to nie to slowo.")
    guess = input("Twoja odpowiedz: ")

if guess == correct:
    print("Zgadza sie! Zgadles!\n")

while guess != correct:
    print("Czy chcesz jakas podpowiedz do tego trudnego slowa?")
    if answer == input("tak"):
        print("Podpowiedz: ", HINTS)


print("Dziekuje za udzial w grze.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")