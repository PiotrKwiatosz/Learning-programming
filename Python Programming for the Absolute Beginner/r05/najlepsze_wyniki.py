# Najlepsze wyniki
# Demonstruje metody listy

scores = []
choice = None

while choice != "0":

    print(
        """
        Najlepsze wyniki
        
        0 - zakoncz
        1 - pokaz wyniki
        2 - dodaj wynik
        3 - usun wynik
        4 - posortuj wyniki
        """
    
    )

    choice = input("Wybierasz: ")
    print()

# zakoncz program
    if choice == "0":
            print("Do widzenia.")

# wypisz tabele najlepszych wynikow
    elif choice == "1":
        print("Najlepszy wynik")
        for score in scores:
            print(score)

# dodaj wynik
    elif choice == "2":
        score = int(input("Jaki wynik uzyskales?: "))
        scores.append(score)

# usun wynik
    elif choice == "3":
        score = int(input("Ktory wynik usunac?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "nie ma na liscie wynikow.")

# posortuj wyniki
    elif choice == "4":
        scores.sort(reverse=True)

# nieznana opcja
    else:
        print("Niestety,", choice, "nie jest prawidlowym wyborem.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")