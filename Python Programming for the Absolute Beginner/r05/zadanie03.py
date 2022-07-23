# Napisz program 'Kto jest Twoim tata?' ktory umozliwi uzytkownikowi
# wprowadzenie imienia i nazwiska osoby (plci meskiej) i przedstawi imie
# i nazwisko jej ojca.

print("\tMozesz tu sprawdzic kto jest Twoim ojciem!")
print("\n\tTylko dla osob plci meskiej!")

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

    while choice == "1":

        name = input("Prosze wprowadz swoje imie: ")
        surname = input("Teraz prosze wprowadz swoje nazwisko: ")
        print(name, surname, "zgadza sie?")
        input("Chcesz jeszcze kogos dodac?: ")


input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")

