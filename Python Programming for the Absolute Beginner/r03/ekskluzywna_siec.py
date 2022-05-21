# Ekskluzywna siec
# Demonstruje operatory logiczne i warunki zlozone

print("\tEkskluzywna Siec Komputerowa")
print("\t   Tylko dla czlonkow!\n")

security = 0

username = ""
while not username:
    username = input("Uztkownik: ")

password = ""
while not password:
    password = input("Haslo: ")

if username == "M.Dawson" and password == "sekret":
    print("Czesc, Mike!")
    security = 5
elif username == "S.Meier" and password == "cywilizacja":
    print("Hej, Sid!")
    security = 3
elif username == "S.Miyamoto" and password == "mariobros":
    print("Co u Ciebie, Shigeru?")
    security = 3
elif username == "W.Wright" and password == "simsowie":
    print("Jak leci, Will?")
    securitiy = 3
elif username == "gosc" or password == "gosc":
    print("Witaj, Gosciu!")
    security = 1
else:
    print("Nieudana proba logowania. Nie jestes taki wyjatkowy.\n")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")