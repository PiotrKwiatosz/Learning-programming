# Krajacz pizzy
# Demonstruje tworzenie wycinkow lancuchoa

word = "pizza"

print(
"""
    'Sciagawka' tworzenia wycinkow
    
    0   1   2   3   4   5
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
    -5  -4  -3  -2  -1      
    
"""
)

print("Wprowadz poczatkowy i koncowy indeks wycinka lancucha 'pizza'.")
print("Aby zakonczyc tworzenie wycinkow, w odpowiedzi na monit 'Poczatek':'\n"
      + "nacisnij klawisz Enter.")

start = None
while start != "":
    start = (input("\nPoczatek: "))

    if start:
        start = int(start)

        finish = int(input("Koniec: "))

        print("word[", start, ":", finish, "] to", end=" ")
        print(word[start:finish])

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")