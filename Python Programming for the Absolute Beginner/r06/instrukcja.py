# Instrukcja
# Demonstruje funkcje tworzone przez programiste

def instructions():
    """Wyswietl instrukcje gry."""
    print(
    """
    Witaj w najwiekszym intelektualnym wyzwaniu wszech czasow, jakims jest gra 
    'Kolko i Krzyzyk'. Bedzie to ostateczna rozgrywka miedzy Twoim ludzkim mozgiem
    a moim krzemowym procesorem.
        
    Swoje posuniecie wskazesz poprzez wprowadzenie liczbe z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z ponizszym schematem:
        
            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8

    Przygotuj sie, Czlowieku. Ostateczna batalia niebawem sie rozpocznie. \n
    """
    )

# main
print("Oto instrukcja do gry 'Kolko i Krzyzyk':")
instructions()
print("Ponownie ta sama instrukcja:")
instructions()
print("Prawdopodobnie teraz juz zrozumiales te gre.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")