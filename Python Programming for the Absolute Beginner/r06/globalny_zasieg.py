# Globalny zasieg
# Demonstruje zmienne globalne

def read_global():
    print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
            "\nfunkcji read_global() wynosi:", value)
            
def shadow_global():
    value = -10
    print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
            "\nfunkcji shadow_global() wynosi:", value)
            
def change_global():
    global value
    value = -10
    print("Wartosc zmiennej value odczytana wewnatrz zakresu lokalnego",
            "\nfunkcji change_global() wynosi:", value)

# glowna czesc programu
# value jest zmienna globalna, poniewaz jestesmy teraz w zakresie globalnym

value = 10
print("W zakresie globalnym wartosc zmiennej value zostala ustawiona na:", value, "\n")

read_global()
print("Po powrocie do zakresu globalnego wartosc zmiennej value nadal wynosi:", value, "\n")

shadow_global()
print("Po powrocie do zakresu globalnego wartosc zmiennej value nadal wynosi:", value, "\n")

change_global()
print("Po powrocie do zakresu globalnego okazuje sie, ze wartosc zmiennej value",
        "\nzmienila sie na:", value)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
