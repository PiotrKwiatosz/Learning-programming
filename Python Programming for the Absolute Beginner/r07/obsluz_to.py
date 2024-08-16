# Obsluz to
# Demonstruje obsluge wyjatkow

# try/except
try:
    num = float(input("Wprowadz liczbe: "))
except:
    print("Wystapil jakis blad!")

# specyfikacja typu wyjatku
try:
    num = float(input("\nWprowadz liczbe: "))
except ValueError:
    print("To nie byla liczba!")

# obsluz kilka typow wyjatkow
print()
for value in (None, "Hej!"):
    try:
        print("Proba konwersji:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Wystapil jakis blad!") 

print()
for value in (None, "Hej!"):
    try:
        print("Proba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Mozliwa jest tylko konwersja lancucha lub liczby!")
    except ValueError:
        print("Mozliwa jest tylko konwesja lancucha cyfr!")

# pobierz argument wyjatku

try:
    num = float(input("\nWprowadz liczbe: "))
except ValueError as e:
    print("To nie byla liczba! Lub wyrazajac to na sposob Pythona...")
    print(e)

# try/except/else
try:
    num = float(input("\nWprowadz liczbe: "))
except ValueError:
    print("To nie byla liczba!")
else:
    print("Wprowadziles liczbe", num)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER")