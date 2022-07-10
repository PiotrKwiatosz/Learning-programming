# Translator slangu komputerowego
# Demonstruje uzywanie slownikow

geek = {"404": "ignorant, od uzywanego w sieci WWW komunikatu o bledzie 404\n - nie znaleziono strony.",
        "Googling": "googlowanie; wyszukiwanie w internecie informacji dotyczacych jakiejs osoby.",
        "Keyboard Plaque": "(skojarzone z kamieniem nazebnym) zanieczyszczenia nagromadzone w klawiaturze komputera.",
        "Link Rot": "(obumieranie linkow) proces, w wyniku ktoregp linki do stron WWW staja sie nieaktualne.",
        "Percussive Maintenance": "(konserwacja perkusyjna) naprawa urzadzenia elektronicznego przez stukniecie.",
        "Uninstalled": "(odinstalowany) zwolniony z pracy; termin szczegolnie popularny w okresie banki internetowej."}

choice = None
while choice != "0":

    print(
    """
    Translator slangu komputerowego
        
    0 - zakoncz
    1 - znajdz termin
    2 - dodaj nowy termin
    3 - zmien definicje terminu
    4 - usun termin
    """
    )

    choice = input("Wybierasz: ")
    print()

    # wyjdz
    if choice == "0":
        print("Zegnaj.")

    # pobierz definicje
    elif choice == "1":
        term = input("Jaki termin mam przetlumaczyc?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "oznacza", definition)
        else:
            print("\nNiestety, nie znam terminu", term)

    # dodaj pare termin-definicja
    elif choice == "2":
        term = input("Jaki termin mam dodac?: ")
        if term not in geek:
            definition = input("\nPodaj deinicje tego terminu: ")
            geek[term] = definition
            print("\nTermin", term, "zostal dodany.")
        else:
            print("\nTen termin juz istnieje! Sprobuj zmienic jego definicje.")
    
    # zmiana definicji istniejacego terminu
    elif choice == "3":
        term = input("Jaki termin mam przedefiniowac?: ")
        if term in geek:
            definition = input("Jaka jest nowa definicja?: ")
            geek[term] = definition
            print("\nTermin", term, "zostal przedefiniowany.")
        else:
            print("\nTen termin nie istnieje! Sprobuj go dodac.")

    # usuniecie pary termin-definicja
    elif choice == "4":
        term = input("Jaki termin mam usunac?: ")
        if term in geek:
            del geek[term]
            print("\nOK, usunalem go", term)
        else:
            print("\nNie moge tego zrobic! Terminu", term, "nie ma w slowniku.")

    # nieznana opcja
    else:
        print("\nNiestety,", choice, "to nieprawidlowy wybor.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
