# Najlepsze wyniki 2.0
# Demonstruje sekwencje zagniezdzone

scores = []

choice = None
while choice != "0":

    print(
        """
        Najlepsze wyniki 2.0
        
        0 - zakoncz
        1 - wyswietl wyniki
        2 - dodaj wynik
        """
    )

    choice = input("Wybierasz: ")
    print()

    # zakoncz
    if choice == "0":
        print("Do widzenia.")

    # wyswietl tabele najlepszych wynikow
    elif choice == "1":
        print("Najlepsze wyniki\n")
        print("GRACZ\tWYNIK")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # dodaj wynik
    elif choice == "2":
        name = input("Podaj nazwe gracza: ")
        score = int(input("Jaki wynik gracz uzyskal?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]     # zachowaj tylko 5 najlepszych wynikow

    # nieznana opcja
    else:
        print("Niestety,", choice, "nie jest prawidlowym wyborem.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
