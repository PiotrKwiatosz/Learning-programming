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
         "pomieszane", 
         "odpowiedz")

# sekwencja podpowiedzi do slow
HINTS = ("Jezyk programowania ktory jest na litere P", 
         "Gram i ana-nas, jak to mozna zlaczyc?", 
         "Male zdrobnienie do imienia wielkiego Apostola", 
         "Jak nielatwy to jaki?", 
         "Jak cos sie miesza to jakie sie staje? I jaki ktos moze byc?", 
         "Pytanie i ...?")

# wybierz losowo jedno slowo z sekwencji
index = random.randint(0,len(WORDS))
word = WORDS[index]
hint = HINTS[index]

# utworz zmienna, by pozniej uzyc jej do sprawdzenia, czy odpowiedz jest poprawna
correct = word

# utworz zmienna aby podpowiedz byla podana tylko raz
given_hint = False

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
print("\nZgadnij, jakie to slowo:", jumble)

guess = input("\nTwoja odpowiedz: ")

while guess != correct and guess != "":
    print("Niestety, to nie to slowo.")
    if  given_hint == False:
        want_hint = input("Czy chcesz podpowiedz? Tak lub nie: ")
        if want_hint.lower() == "tak" or want_hint.lower() == "t":
                print("Podpowiedz: ", hint)
                given_hint = True

    guess = input("Twoja odpowiedz: ")

if guess == correct:
    print("Zgadza sie! Zgadles!\n")
    if given_hint == False:
        print("Zdobyles maksymalna ilosc punktow - 10!")
    else:
        print("Zdobyle 5 punktow z 10, bo skorzystales z podpowiedzi.")


print("Dziekuje za udzial w grze.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")