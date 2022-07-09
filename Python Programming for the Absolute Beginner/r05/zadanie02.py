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
            points, name = entry
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
            5 - Usuwanie punktow
            """
        )
    choice = None
    while choice != "0":

        choice = input("Wybierasz: ")
        print()
        used = []
        points != 30

        # wyjdz
        if choice == "0":
            print("Powrot do glownego menu")

        # wybrana SILA
        elif choice == "1":
            point = int(input("Ile punktow chcesz przeznaczyc na SILE? :"))
            strenght = point
            points.append(strenght)
            points.sort(reverse=True)
            points = points[:30]
            used.append(points)    
        
         # wybrana ZDROWIE
        elif choice == "2":
            point = int(input("Ile punktow chcesz przeznaczyc na ZDROWIE? :"))
            health = point
            points.append(health)
            points.sort(reverse=True)
            points = points[:30]
            used.append(points)

        # wybrana MADROSC
        elif choice == "3":
            point = int(input("Ile punktow chcesz przeznaczyc na MADROSC? :"))
            wisdom = point
            points.append(wisdom)
            points.sort(reverse=True)
            points = points[:30]
            used.append(points)

        # wybrana ZRECZNOSC
        elif choice == "4":
            point = int(input("Ile punktow chcesz przeznaczyc na ZRECZNOSC? :"))
            skill = point
            points.append(skill)
            points.sort(reverse=True)
            points = points[:30]
            used.append(points)

        elif choice == "5":
            print("Skad chcesz usunac punkty? :")

        elif points == 0:
            print("Niestety nie masz juz punktow")
            break

        # nieznana opcja
        else:
            print("Niestety,", choice, "nie jest prawidlowa")
            
    
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

            

