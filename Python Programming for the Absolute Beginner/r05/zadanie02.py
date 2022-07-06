# Napisz program 'Kreator postaci' do gry RPG (z podzalem na role).
# Gracz powinien otrzymac pule 30 punktow, ktore moze spozytkowac na 4 atrybuty:
# -sila, -zdrowie, -madrosc, -zrecznosc
# Gracz powinien miec mozliwosc przeznaczanoa punktow z puli na dowolny atrybut, 
# jak rowniez mozliwosc odbierania punktow przypisanych do atrybutu i
# przekazywanie ich spowrotem do puli

points = []

choice = None
while choice != "O":

    print(
        """
        
        Kreator postaci do magicznego swiata!
        Dostajesz -> 30 <- punktow ktore mozesz rozdysponowac na 4 wartosci
        -sila, -zdrowie, -madrosc i -zreczonsc.
        Wybierz co chcesz zrobic:

        0 - zakoncz
        1 - wyswietl na co przyznales punkty
        2 - wybierz kategorie na co chcesz dodac punkty
        """
    )

    choice = input("Wybierasz: ")
    print()

    # zakoncz
    if choice == "0":
        print("Zegnaj!")

    # wyswietl tabele na co przyznales punkty
    elif choice == "1":
        print("Punkty przyznane na\n: ")
        print("WARTOSC\tPUNKTY")
        for entry in points:
            point, name = entry
            print(name, "\t", point)

    # dodaj punkty
    elif choice == "2":
        print(
            """
            
            Wartosci na ktore mozesz przeznaczyc punkty:
            
            0 - wyjdz
            1 - SILA
            2 - ZDROWIE
            3 - MADROSC
            4 - ZRECZNOSC
            """
        )

        choice = input("Wybierasz: ")
        print()

        # wyjdz
        if choice == "0":
            print("Powrot do glownego menu")

        # wybrana SILA
        elif choice == "1":
            score = int(input("Ile punktow chcesz przeznaczyc na SILE? :"))
            strenght = score
            scores.append(strenght)
            scores.sort(reverse=True)
            scores = scores[:30]
        
         # wybrana ZDROWIE
        elif choice == "2":
            score = int(input("Ile punktow chcesz przeznaczyc na ZDROWIE? :"))
            health = score
            scores.append(health)
            scores.sort(reverse=True)
            scores = scores[:strenght]
            
        # wybrana MADROSC
        elif choice == "3":
            score = int(input("Ile punktow chcesz przeznaczyc na MADROSC? :"))
            wisdom = score
            scores.append(wisdom)
            scores.sort(reverse=True)
            scores = scores[:health]

        # wybrana ZRECZNOSC
        elif choice == "4":
            score = int(input("Ile punktow chcesz przeznaczyc na ZRECZNOSC? :"))
            skill = score
            scores.append(skill)
            scores.sort(reverse=True)
            scores = scores[:wisdom]


        # nieznana opcja
        else:
            print("Niestety,", choice, "nie jest prawidlowa")
            
    
    
    input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

            

