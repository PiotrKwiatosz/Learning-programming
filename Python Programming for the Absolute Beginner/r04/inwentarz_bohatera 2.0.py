# Inwentarz bohatea 2.0
# Demonstruje krotki

# utworz krotke zawierajaca pewne elementy i wyswietl jej zawartosc
# za pomoca petli
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napoj uzdrawiajacy")
print("Elementy Twojego inwentarza:")
for item in inventory:
    print(item)

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# wyswietl dlugosc krotki
print("Twoj dobytek zawieta", len(inventory), "elementy(-ow).")

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# s[rawdz czy element nalezy do krotki, za pomoca operatora 'in'
if "napoj uzdrawiajacy" in inventory:
    print("Dozyjesz dnia, w ktorym stoczysz walke.")

# wyswietl jeden element wskazany przez indeks
index = int(input("\nWprowadz indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje sie", inventory[index])

# wyswietl wycinek
start = int(input("\nWprowadz indeks wyznaczajacy poczatek wycinka: "))
finish = int(input("\nWprowadz indeks wyznaczajacy koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# dokonaj konkatencji dwoch krotek

chest = ("zloto", "klejnoty")
print("Znajdujesz skrzynie, ktora zawieta:")
print(chest)
print("Dodajesz zawartosc skrzyni do swojego inwentarza.")
inventory += chest
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
