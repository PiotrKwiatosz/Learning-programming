# POPRAWIONE Wymieszane litery
# Komputer wybiera losowo slowo a potem miesza w nim litery
# Gracz powinien odgadnac pierwotne slowo

# Gracz ma teraz mozliwosc zobaczenia podpowiedzi
# Dodany system punktacji

import random

# utworz sekwencje slow do wyboru
WORDS = ("python", 
         "anagram", 
         "piotrek", 
         "trudny", 
         "pomieszany", 
         "odpowiedz")

# sekwencja podpowiedzi do slow
HINTS = ("Jezyk programowania ktory jest na litere P", 
         "Gram i ana-nas, jak to mozna zlaczyc?", 
         "Male zdrobnienie do imienia wielkiego Apostola", 
         "Jak nielatwy to jaki?", 
         "Jak cos sie miesza to jakie sie staje? I jaki ktos moze byc?", 
         "Pytanie i ...?")

# konkatecja czyli laczenie zbiorow
WORDS = HINTS

# Odpowiedz tak czy nie
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

if  guess != correct:
    print("Czy chcesz jakas podpowiedz do tego trudnego slowa?")
    input("Tak czy nie?")
    if answer.lower == "tak":
        for word in  WORDS:
            print("Podpowiedz :", hint)
    else:
        print("Nie ma takiego slowa")
guess = input("\nTwoja odpowiedz: ")


print("Dziekuje za udzial w grze.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")