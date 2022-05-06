# Uczestnik funduszu powierniczegp - niepoprawna wersja
# Demonstruje konwersje typow

print(
"""
                Uczestnik funduszu powierniczego
                
Sumuje Twoje miesieczne wydatki, zeby Twoj fundusz powierniczy sie nie wyczerpal
(bo wtedy bylbys zmuszony do podjecia prawdziwej pracy).

Wprowadz swoje wymagane miesieczne koszty.
Poniewaz jestes bogaty, zignoruj grosze i swoje kwoty podaj w pelnych zlotych.

"""
)

car = input("Serwi Mercedesa: ")
car = int(car)

rent = int(input("Apartament w Srodmiesciu: "))
jet = int(input("Wynajem prywatnego samolotu: "))
gifts = int(input("Podarunki: "))
food = int(input("Obiady w restauracjach: "))
staff = int(input("Personel (sluzba domowa, kucharz, kierowca, asystent): "))
guru = int(input("Osobisty guru i coach: "))
games = int(input("Gry komputerowe: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nOgolem:", total)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")