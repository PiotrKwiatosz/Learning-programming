# Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
# gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
# gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
# odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
# sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.

print("Witaj graczu! Pobawimy sie teraz w znana gre 'Jaka to liczba'")
print("Teraz zamienimy sie rolami i to Ty bedziesz wymyslal liczbe a ja bede ja odgadywal")
print("Wiec wymysl sobie teraz jakas liczbe z przedzialu od 1 do 100")
print("Ale mam na to tylko 10 prob")

import random

number = random.randint(1,100)
guess = int(input("Czy ta liczba to: ?"))

answer1 = ""
while not answer1:
    answer1 = input("Tak")
answer2 = ""
while not answer2:
    answer = input("Nie")
    
tries = 10

while tries > 0:
    while number != guess:
            print("Czy ta liczba to: ", number, "?")
            if answer == "Nie":
                print("Za duza?")
                if input(answer1):
                    print("Czy ta liczba to: ", number, " ?")
                elif input(answer2):
                    print("Czy ta liczba to ", number, " ?")
            elif answer == "Tak":
                print("Udalo mi sie! Twoja liczba to: ", number, "Super bylo!")
                print("Aby ja odgadnac porzebowalem ", 10 - tries, " prob!")
                break
            else:
                print("Nie rozumiem Cie...")

    guess = print("Czy ta liczba to: ?")
    tries -= 1

if tries == 0:
    print("\nKONIEC! Nie udalo mi sie jej zgadnac w 10 probach...")
    print("\nUciekla i nie zlapalem jej...")
    print("\n\tA byla to: ->", number, "<- liczba...?")
    print("\nMusze postrac sie bardziej :(")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


