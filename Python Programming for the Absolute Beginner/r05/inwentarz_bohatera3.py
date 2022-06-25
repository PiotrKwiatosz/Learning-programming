# Inwentarz bohatera 3.0
# Demonstruje listy

# utworz liste zawierajaca pewne elementy i wyswietl jej zawartosc
# za pomoca petli 'for'
inventory = ["miecz", "zbroja", "tarcza", "napoj uzdrawiajacy"]
print("Elementy Twojego inwentarza:")
for item in inventory:
    print(item)

# wyswietl dlugosc listy
print("Twoj dobytek zawiera", len(inventory), "elementy-(ow).")

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# sprawdz, czy element nalezy do listy, za pomoca operatora 'in'
if "napoj uzdrawiajacy" in inventory:
    print("Dozyjesz dnia, w ktorym stoczysz walke.")

# wyswietl jeden element wskazany przez indeks
index = int(input("\nWprowadz indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje sie", inventory[index])

# wyswietl wycinek
start = int(input("\nWprowadz indeks wyznaczajacy poczatek wycinka: "))
finish = int(input("Wprowadz indeks wyznaczajacy koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# dokonaj konkatenacji dwoch list
chest = ["zloto", "klejnoty"]
print("Znajdujesz skrzynie, ktora zawiera:")
print(chest)
print("Dodajesz zawartosc skrzyni do swojego inwentarza.")
inventory += chest
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# przypisz poprzez indeks
print("Wymieniasz swoj miecz na kusze.")
inventory[0] = "kusza"
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# przypisz poprzez wycinek
print("Zuzywasz swoje zloto i klejnoty na zakup kuli do wrozenia.")
inventory[4:6] = ["kula do wrozenia"]
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# usun element
print("W wielkiej bitwie Twoja tarcza zostaje zniszczona.")
del inventory[2]
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\nAby kontynuowac gre, nacisnij klawisz ENTER.")

# usun wycinek
print("Twoja kusza i zbroja zostaly skradziony przez zlodziei.")
del inventory[:2]
print("Twoj aktualny inwentarz to:")
print(inventory)

input("\nAby zakonczyc program, nacisnij klawisz ENTER.")