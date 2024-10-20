import json

def zapisz_wyniki(nazwa_uzytkownika, wynik):
    dane = {
        'uzytkownik': nazwa_uzytkownika,
        'wynik': wynik
    }
    
    # Zapisz dane do pliku JSON
    with open('wyniki_quizu.json', 'a') as plik:
        json.dump(dane, plik)
        plik.write('\n')  # Zapis każdej odpowiedzi w nowej linii

def quiz():
    # Lista pytań z odpowiedziami (pytanie, poprawna odpowiedź)
    pytania = [
        ("Ile kontynentów jest na świecie?", "7"),
        ("Jaka jest stolica Francji?", "Paryż"),
        ("Ile wynosi liczba Pi z dokładnością do dwóch miejsc po przecinku?", "3.14"),
        ("W którym roku Polska dołączyła do Unii Europejskiej?", "2004")
    ]

    wynik = 0
    
    # Pobierz nazwę użytkownika
    nazwa_uzytkownika = input("Podaj swoje imię: ")

    print("\nRozpoczynamy quiz!\n")

    for i, (pytanie, poprawna_odpowiedz) in enumerate(pytania, 1):
        print(f"Pytanie {i}: {pytanie}")
        odpowiedz = input("Twoja odpowiedź: ")

        if odpowiedz.lower() == poprawna_odpowiedz.lower():
            print("Poprawna odpowiedź!\n")
            wynik += 1
        else:
            print(f"Zła odpowiedź. Poprawna odpowiedź to: {poprawna_odpowiedz}\n")
    
    print(f"Koniec quizu! {nazwa_uzytkownika}, Twój wynik to: {wynik}/{len(pytania)}")

    # Zapisz wynik do pliku
    zapisz_wyniki(nazwa_uzytkownika, wynik)

# Uruchom quiz
if __name__ == "__main__":
    quiz()