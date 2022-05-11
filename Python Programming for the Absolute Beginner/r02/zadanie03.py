# Rozdzial 2
# Zadanie 3

# Kalkulator napiwku

print("Witaj! Jestem kalkulatorem napiwku, ktory oblicza jaki napiwek powinienes dac. W wysokosci 15% albo 20%")

rachunek = input("Prosze podaj ogolna sume z rachunku wystawionego przez restauracje: ")
rachunek = int(rachunek)

napiwek_1 = int(rachunek * 0.15)
napiwek_2 = int(rachunek * 0.25)

print("Oto napiwki jakie powinienes dac, wybor nalezy do Ciebie: ")
print(napiwek_1)
print(napiwek_2)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")