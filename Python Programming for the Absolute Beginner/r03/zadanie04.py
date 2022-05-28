# Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
# gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
# gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
# odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
# sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.

import random

print("Witaj graczu! Pobawimy sie teraz w znana gre 'Jaka to liczba'")
print("Teraz zamienimy sie rolami i to Ty bedziesz wymyslal liczbe a ja bede ja odgadywal")
print("Wiec wymysl sobie teraz jakas liczbe z przedzialu od 1 do 100")
print("Ale mam na to tylko 10 prob")

y = input("\nPomyśl o jakiejś liczbie (zapisz liczbę w pamięci): ")
number = random.randint(1,100)
tries = 10

while number != y:
    number = random.randint(1,100)
    tries > 0
    if number == y:
            print("Twoja liczba to", number, "Udalo mi sie!")
            break
    print("Czy miałeś na myśli liczbę", number, "?")

    tries -= 1

    reply = input("tak/nie: ")
    if reply == "tak":
        print("widzisz? Udalo mi sie! :D")
        print("Super!")
        print("Aby ja odgadnac porzebowalem ", 10 - tries, " prob!")
        print("")
        break

if tries == 0:
    print("\nKONIEC! Nie udalo mi sie jej zgadnac w 10 probach...")
    print("\nUciekla i nie zlapalem jej...")
    print("\n\tA byla to: ->", number, "<- liczba...?")
    print("\nMusze postrac sie bardziej :(")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


