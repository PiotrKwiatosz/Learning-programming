# Napisz program 'Kto jest Twoim tata?' ktory umozliwi uzytkownikowi
# wprowadzenie imienia i nazwiska osoby (plci meskiej) i przedstawi imie
# i nazwisko jej ojca.

print("\tMozesz tu sprawdzic kto jest Twoim ojciem!")
print("\n\tTylko dla osob plci meskiej!")

sf = {"Kacper Kwiatosz" : "Piotr Kwiatosz", "Funtek Funt" : "Funtoslaw Funt"}
son = ''
father = ''
choice = None

while choice != "0":
    
    print("""
    Wybierz co chcesz zrobic:
    
    0 - Wyjsc
    1 - Zobacz pary Synn-Ojciec
    2 - Dodaj pare Syn-Ojciec
    3 - Zamien pare Syn-Ojciec
    4 - Usuwanie par Syn-Ojciec
    """)

    choice = input("Ktora opcje wybierasz?: ")
    print()

    if choice == "0":
        print("Zegnaj!")

    elif choice == "1":
        if sf == {}:
            print("Baza aktualnie jest pusta, dodaj kogos!")
            continue
        else:
            for son, father in sf.items():
                print(son.title(), "jest", father.title(), "synem.")

    elif choice == "2":
        son = input("Kto jest synem? ")
        son = son.lower()
        if son in sf:
            print("Ten syn juz istnieje! Zamiast tego sprobuj zastapic")
            continue
        father = input("Kto jest ojcem? ")
        father = father.lower()
        sf[son] = father
        print("\n", son.title(), "jest", father.title(), "synem")

    elif choice == "3":
        sorf = input("Czy znasz syna lub ojca? ")
        sorf = sorf.lower
        while sorf != "son" and sorf != "father":
            print("Przeprasza, prosze napisz syna lub ojca")
            sorf = input("Czy znasz syna lub ojca? ")
            sorf = sorf.lower
        
        if sorf == "son":
            son = input("Kto jest synem? ")
            son = son.lower
            if son in sf.keys():
                print("Ten obecny ojciec jest" , sf[son].title())
                father = input("Kim chcesz go zamienic? ")
                father = father.lower()
                sf[son] = father
                print("Ojcem ", son.title(), "jest teraz ", father.title())
            elif son not in sf.keys():
                print("Ten syn nie istnieje. Dlaczego go moze nie dodasz?")
                continue
        
        if sorf == "father":
            father = input("Kto jest ojcem? ")
            father = father.lower
            if father in sf.values():
                for son, dad in sf.items:
                    if dad == father:
                        print("Ten obecny syn jest ", son.title())
                        del sf[son]
                        son = input("Kim chcesz go zamienic? ")
                        sf[son] = father
                        print(son.title(), "jest", father.title(), "synem.")
                        break
            elif father not in sf.values:
                print(father, "nie istnieje. Dlaczego go nie dodasz?")

    elif choice == "4":
        son = input("Kto jest synem? ")
        son = son.lower()
        if son not in sf:
            print(son, "nie istniej!. Byc mozesz juz go usunales...")
            continue
        else:
            print(son.title(), "i ", sf[son].title(), "zostali usunieci")
            del sf[son]
    
    else:
        print("Przepraszam, nieprawidlowy wybor.")



input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")

