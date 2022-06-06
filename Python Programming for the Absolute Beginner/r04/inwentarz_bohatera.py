# Inwentarz bohatera
# Demonstruje tworzenie 'krotek'

# utworz pusta krotke
inventory = ()

# potraktuj krotke jako warunek
if not inventory:
    print("Masz puste rece. Nie posiadasz niczego.")

input("\nAby kontynuowac misje, nacisnij klawisz ENTER.")

# utworz krotke zawierajaca pewne elementy
inventory = ("miesz",
             "zbroja",
             "tarza",
             "napoj uzdrawiajacy")

# wyswietl krotke
print("\nWykaz zawartosci krotki:")
print(inventory)

# wyswietl kazdy element krotki
print("\nElementy Twojego wyposazenia:")
for item in inventory:
    print(item)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")