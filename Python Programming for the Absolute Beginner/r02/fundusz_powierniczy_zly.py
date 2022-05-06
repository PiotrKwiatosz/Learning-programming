# Uczestnik funduszu powierniczegp - niepoprawna wersja
# Demonstruje blad logiczny

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
rent = input("Apartament w Srodmiesciu: ")
jet = input("Wynajem prywatnego samolotu: ")
gifts = input("Podarunki: ")
food = input("Obiady w restauracjach: ")
staff = input("Personel (sluzba domowa, kucharz, kierowca, asystent): ")
guru = input("Osobisty guru i coach: ")
games = input("Gry komputerowe: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nOgolem:", total)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")