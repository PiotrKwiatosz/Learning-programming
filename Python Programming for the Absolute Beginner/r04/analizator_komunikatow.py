# Analizator komunikatow
# Demonstruje funkcje 'len()' i operatora 'in'

message = input("Wprowadz komunikat: ")

print("\nDlugosc Twojego komunikatu wynosi:", len(message))

print("\nNajczesciej uzywana litera w jezyku polskim, 'a',")
if "a" in message:
    print("wystapila w Twoim komunikacie.")
else:
    print("nie wystapila w Twoim komunikacie.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")