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
points = 30
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
    print("\nJest ", points, "punktow w schowku.")
    print(choice_sentence)
    choice = input("Wybierasz: ")
    print()

    while choice != "0" and choice != "1" and choice !="2":
        print("Zly wybor")
        print(choice_sentence)
        choice = input("Wybierasz: ")
    
    # dodanie punktow do atrybutu
    while choice == "1":
        if points == 0:  # nie ma juz punktow
            print("Przykro mi, ale nie masz punktow. Sprobuj dodac tu troche punktow")
            break
        print("\nMasz ", points, " punktow w schowku")
        print("\nNa jaki atrybut chcesz je przyznac?")
        print(attribute_list)
        att_to_change = input("Atrybut do zmienienia: ")
        while (att_to_change != attribute_list):
            print("To jest nieprawidlowy wybor.")
            print("Na ktory atrybut chcesz dodac punkty?")
            print(attribute_list)
            att_to_change = input("Atrybut do zmiany: ")


    if choice == "0":
        print("\nZegnaj.")





# nieznana opcja
#    else:
#        print("Niestety,", choice, "nie jest prawidlowa")
            
    
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")

            

