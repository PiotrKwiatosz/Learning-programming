# Rozdzial 2
# Zadanie 4

# Sprzedawca samochodow

print("Witam, prosze podaj cene wybranego samochodu,")
print("a ja oblicze dla Ciebie wszystkkie inne dodatkowe oplaty.")
print("Podam Ci koncowa, faktyczna cene wybranego samochodu")

price = int(input("\nProsze podaj cene: "))

tax = int(price * 0.30)
# print(("\nPodate: "), tax)
reg_fee = int(price * 0.18)
# print("Oplata rejestracyjna: ", reg_fee)
commision = int(price + 699)
# print("Prowizja dealera: ", commision)
delivery = int(price + 199) 
# print("Dostawa: ", delivery)

final_price = price + tax + reg_fee + commision + delivery

print("Ostateczna cena wybranego samochodu to:", final_price)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")
