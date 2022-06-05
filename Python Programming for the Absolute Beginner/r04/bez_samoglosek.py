# Bez samoglosek
# Demonstruje tworzenie nowych lancuchow przy uzyciu petli 'for'

message = input("Wprowadz komunikat: ")
new_message = ""
VOWELS = "aąeęioóuy"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Zostal utworzony nowy lancuch: ", new_message)

print("\nTwoj komunikat bez samoglosek to:", new_message)

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")