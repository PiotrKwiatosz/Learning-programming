# Program ktory wczytuje komunikat od uzytkownika
# Nastepnie wypisuje go w odwrotnej kolejnosci

message = input("Wprowadz swoj komunikat: ")

revmessage = ""

print()
for letter in message:
    revmessage = letter + revmessage

print("\nTen komunikat w odwrotnej kolejnosci to: ", revmessage)


input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")