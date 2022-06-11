# Program ktory liczy za uzytkownika
# Wprowadza sie liczbe poczatkowa i startowa oraz odstep miedzy liczbami

print("Witaj, oto program ktory liczy za Ciebie, odkad dokad chcesz")
print("Wprowadz liczbe poczatkowa i koncowa oraz separator co ile:")

start = int(input("\nPoczatek: "))
finish = int(input("Koniec: "))
separator = int(input("Co ile ma byc liczone: "))

for i in range(start, finish, separator):
    print(i, end=" ")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
