# Wybredny licznik
# Demonstruje instrukcje 'break' i 'continue'

count = 0
while True:
    count += 1
    # zakoncz petle jesli wartosc zmiennej count jest wieksza niz 10
    if count > 10:
        break
    # pomin liczbe 5
    if count == 5:
        continue
    print(count)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")