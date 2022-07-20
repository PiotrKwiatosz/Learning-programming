# Napisz program 'Kreator postaci' do gry RPG (z podzalem na role).
# Gracz powinien otrzymac pule 30 punktow, ktore moze spozytkowac na 4 atrybuty:
# -Sila, -Zdrowie, -Madrosc, -Zrecznosc
# Gracz powinien miec mozliwosc przeznaczanoa punktow z puli na dowolny atrybut, 
# jak rowniez mozliwosc odbierania punktow przypisanych do atrybutu i
# przekazywanie ich spowrotem do puli


print("""
                KREATOR POSTACI DO MAGICZNEGO SWIATA!
        
        Dostajesz -> 30 <- punktow ktore mozesz rozdysponowac na 4 wartosci:
            Sila, Zdrowie, Madrosc i Zreczonsc.
        Jesli zmienisz zdanie, mozesz zabrac punkty z dangeo atrybutu i dac je spowrotem
        do magazynu.
"""
    )

attributes = {'strength':0, 'health':0, 'wisdom':0, 'dexterity':0}
pool = 30
choice = None
spend = None

choice_sentence = """
\n\nWybierz co chcesz zrobic:

0 - Zakoncz
1 - Wyswietl na co przyznales punkty
2 - Wybierz kategorie na co chcesz dodac punkty
"""

attribute_list = """
\tStrength
\tHealth
\tWisdom
\tDexterity
"""

while choice != "0":

    print("\nTwoj charakter ma takie atrybuty:")
    for attribute, points in attributes.items():
        print("\t", attribute.title(), ":\t ", points)
    print("\nJest ", pool, "punktow w schowku.")
    print(choice_sentence)
    choice = input("Wybierasz: ")
    print()

    while choice != "0" and choice != "1" and choice !="2":
        print("Zly wybor")
        print(choice_sentence)
        choice = input("Wybierasz: ")
    
    while choice == "1":         # dodanie punktow do atrybutu
        if pool == 0:            # nie ma juz punktow
            print("Przykro mi, ale nie masz punktow. Sprobuj dodac tu troche punktow")
            break
        print("\nMasz ", pool, " punktow w schowku")
        print("\nNa jaki atrybut chcesz je przyznac?")
        print(attribute_list)
        att_to_change = input("Atrybut do zmienienia: ")
        while (att_to_change.title() != "Strength" and
            att_to_change.title() != "Health" and
            att_to_change.title() != "Wisdom" and
            att_to_change.title() != "Dexterity"):
            print("To jest nieprawidlowy wybor.")
            print("Na ktory atrybut chcesz dodac punkty?")
            print(attribute_list)
            att_to_change = input("Atrybut do zmiany: ")
        else:
            points = int(input("Ile punktow chcesz przyznac?: "))
            while points > pool:
                print("To jest za duzo punktow. Masz", pool, "do przyznania")
                points = int(input("Ile punktow chcesz przyznac?: "))
        attributes[att_to_change] += points
        pool -= points
        print("\nTwoje atrybuty")
        for attribute, points in attributes.items():
            print("\t", attribute.title(), ":  \t", points)
        if pool == 0:
            print("\nWydales juz wszystkie swoje punkty.")
            choice = None
            break
        another_change = input("Chcesz zmienic inny atrybut? Tak czy Nie: ")
        while another_change.title() != "Yes" and another_change.title() != "No":
            print("Nieprawidlowy wybor.")
            another_change = input("Chcesz zmienic inny atrybut? Tak czy Nie: ")
        if another_change.title() == "No":
            break

    while choice == "2":    # dodaj punkty do schowka
        if pool == 30:      # schowek jest pelny
            print("\nPrzepraszam, nie masz zadnych punktow w swoich atrybutach."
            "\nSprobuj najpierw dodac jakies punkty do swoich atrybutow.")
            break
        print("\nZ jakiego atrybutu chcesz zabrac punkty?")
        for attribute, points in attribute.items():
            print(attribute.title(), ":\t", points)
        att_to_change = input("Wybor: ")
        while (att_to_change.title() != "Strength" and
            att_to_change.title() != "Health" and
            att_to_change.title() != "Wisdom" and
            att_to_change.title() != "Dexterity"):
            print("\nTo jest nieprawidlowy wybor.")
            print("\nZ ktorego atrybutu chcesz zabrac punkty?")
            for attribute, points in attribute.items():
                print(attribute.title(), ":\t", points)
            att_to_change = input("Wybor: ")
        while attributes[att_to_change] == 0:       # zadneg punkty nie moga byc usuniete
            print("Nie masz zadnych punktow w tym atrybucie.")
            att_to_change = input("Wybor: ")
            while (att_to_change.title() != "Strength" and
                att_to_change.title() != "Health" and
                att_to_change.title() != "Wisdom" and
                att_to_change.title() != "Dexterity"):
                print("\nTo jest nieprawidlowy wybor.")
                print("\nZ ktorego atrybutu chcesz zabrac punkty?")
                att_to_change = input("Wybor: ")
        points = int(input("\nJak duzo punktow chcesz usunac?: "))
        while points > attributes[att_to_change]:   #za malo punktow w atrybucie
            print("Przepraszam, to jest za duzo punktow! Masz tylko", attributes[att_to_change], "w", att_to_change)
            points = int(input("\nJak duzo pinktow chcesz usunac?: "))
        print("OK!")
        pool += points
        attributes[att_to_change] -= points
        print("Teraz masz ", pool, "dodatkowo punktow w swoim schowku.")
        another_change = input("\nChcesz zmienic inny atrybut? Tak czy Nie?: ")
        while another_change.title() != "Tak" and another_change.title() != "Nie":
            print("\nTo jest nieprawidlowy wybor.")
            another_change = input("\nChcesz zmienic inny atrybut? Tak czy Nie?: ")
        if another_change.title() == "Nie":
            break

print("Żegnaj!")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")        