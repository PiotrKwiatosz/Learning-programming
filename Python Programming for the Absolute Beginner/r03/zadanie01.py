# Program ktory symuluje ciasteczko z wrozba.
# Program powinien wyswietlic 1 z 5 niepowtarzalnych przepowiednim,
# dokonujac losowego wyboru przy kazdym uruchomieniu

import random

print("Witaj w wirtualnym 'Ciasteczku z Przepowiedniami'!")
print("Ugryz (-> Nacisnij klawisz ENTER <-) ciasteczko i sprawdz przepowiednie.\n")
input("Twoja ciasteczkowa przepowiednia to: \n")

cookie = random.randint(1, 5)

if cookie == 1:
    # przepowiednia 1
    print( \
        """"
        Nie stawiaj czoła rzeczywistości. Odbij się od niej.
        """)

elif cookie == 2:
    # przepowiednia 2
    print( \
        """
        Kto urodził się kurą, orłem nie umrze.
        """)

elif cookie == 3:
    # przepowiednia 3
    print( \
        """
        Szczęście, którego szukasz, jest w drugim ciasteczku.
        """)

elif cookie == 4:
    print( \
        """
        Gdy widzisz mędrca, myśl o tym, by mu dorównać. Gdy widzisz tego, komu brak rozsądku, zastanów się nad samym sobą.
        """)

elif cookie == 5:
    print( \
        """
        Nie oglądaj się za siebie.
        """)

else:
    print("\tUgryz ciasteczko, bo ucieknie!")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")


