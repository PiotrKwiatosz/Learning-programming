# Napisz program 'Kto jest Twoim tata?' ktory umozliwi uzytkownikowi
# wprowadzenie imienia i nazwiska osoby (plci meskiej) i przedstawi imie
# i nazwisko jej ojca.

import string


print("\tMozesz tu sprawdzic kto jest Twoim ojciem!")
print("\n\tTylko dla osob plci meskiej!")

names = {"Buboslaw" : "Bubkowski", "Funtoslaw" : "Funt"}
surnames = 0
choice = None
while choice != "0":
    
    print("""
    Wybierz co chcesz zrobic:
    
    0 - Wyjsc
    1 - Dodawanie imienia i nazwiska
    2 - Edytowanie imienia i nazwiska
    3 - Usuwanie par syn-ojciec
    """)

    choice = input("Wybierasz: ")
    print()

    while choice == "0":
        print("Zegnaj!")

    while choice == "1":
        name = input("Prosze wprowadz imie: ")
        if name not in names:
            surname = input("Teraz prosze wprowadz nazwisko: ")
            names[name] = surname
            print("Osoba: ", names, "zostala dodana")
        add = input("Chcesz jeszcze kogos dodac?: Tak czy Nie? ")
        if add != "Tak" and add != "Nie":
            print("Nieprawidlowy wybor")
            add = input("Chcesz jeszcze kogos dodac?: Tak czy Nie? ")
        if add == "Nie":
            break

    while choice == "2":
        print("Jakie imie z podanej listy chcesz edyowac?: ")
        print(names)
        input("Podaj numer imienia: ")



input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")

