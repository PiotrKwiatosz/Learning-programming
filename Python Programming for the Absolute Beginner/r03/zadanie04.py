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
guess = print("Czy ta liczba to: ", number, " ?")
tries = 10

answer = ""
while not answer:
    answer = input("Tak?")
     
while not answer:
    answer = input("Nie?")


while tries > 0:
    while number != guess:
        print("Czy ta liczba to: ", number, "?")
        if answer == "Nie":
            print("Za duza?")
            input("")
            if answer == "Tak":
                print("Czy ta liczba to: ", random.randint(1,100) ,"?")
            elif answer == "Nie":
                print("Za mala?")
                input("")
                if answer == "Tak":
                    print("Czy ta liczba to: ", random.randint(1,100), " ?")
        elif answer == "Tak":
            print("Udalo mi sie! Twoja liczba to: ", number, "Super bylo!")
            print("Aby ja odgadnac porzebowalem ", 10 - tries, " prob!")
            break
        else:
            print("Nie rozumiem Cie...")
            break

    guess = print("Czy ta liczba to: ", number, " ?")
    tries -= 1

if tries == 0:
    print("\nKONIEC! Nie udalo mi sie jej zgadnac w 10 probach...")
    print("\nUciekla i nie zlapalem jej...")
    print("\n\tA byla to: ->", number, "<- liczba...?")
    print("\nMusze postrac sie bardziej :(")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


