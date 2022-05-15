# Komputer nastrojow
# Demonstruje klauzule "elif"

import random

print("Wyczuwam Twoja energie. Twoje prawdziwe emocje znajduja odbicie na moim ekranie.")
print("Jestes...")

mood = random.randint(1,3)

if mood ==1:
    # szczesliwy
    print( \
     """
        --------
        |       |
        | O   O |
        |   <   |
        |       |
        | .   . |
        |  ` `  |
        --------
    """)

elif mood ==2:
    #obojetny
    print( \
     """
        --------
        |       |
        | O   O |
        |   <   |
        |       |
        | ----- |
        |       |
        --------
     """)
        
elif mood ==3:
     # smutny
     print( \
     """
        --------
        |       |
        | O   O |
        |   <   |
        |       |
        |  .'.  |
        | '   ' |
        --------
     """)
else:
   print("Nieprawidlowa wartosc nastroju! (Musisz byc naprawde w zlym humorze).")
        
print("...dzisiaj.")
    
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")