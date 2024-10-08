# Kolko i krzyzyk
# Komputer gra w kolko i krzyzyk przeciwko czlowiekowi

# stale globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Wyswietl instrukcje gry."""
    print(
        """
        Witaj w najwiekszym intelektualnym wyzwaniu wszech czasow, jakim jest gra 'Kolko i krzyzyk'. Bedzie to ostateczna rozgrywka miedzy Twoim ludzkim mozgiem a moim krzemowym procesorem.

        Swoje posuniecie wskazesz poprzez wprowadzenie liczby z zakresu 0 - 8.
        Liczba ta odpowiada pozycji na planszy zgodnie z ponizszym schematem:

                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8

        Przygotuj sie, Czlowieku. Ostateczna batalia niebawem sie rozpocznie. \n
        """
        )

def ask_yes_no(question):
    """Zadaj pytanie, na ktore mozna odpowiedziec tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Popros o podanie liczy z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Ustal, czy pierwszy ruch nalezy do gracza czy do komputera."""
    go_first = ask_yes_no("Czy chcesz miec prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWiec pierwszy ruch nalezy do Ciebie.        Bedzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("\nTwoja odwaga Cie zgubi... Ja wykonuje pierwszy ruch.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Utworz nowa plansze gry."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyswietl plansze gry na ekranie."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Utworz liste prawidlowych ruchow."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Ustal zwyciezce gry."""
    WAYS_TO_WIN = ((0, 1, 2),
                    (3, 4, 5),
                    (6, 7, 8),
                    (0, 3, 6),
                    (1, 4, 7),
                    (2, 5, 8),
                    (0, 4, 8),
                    (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    """Odczytaj ruch czlowieka."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki bedzie Twoj ruch? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest juz zajete, niemadry Czlowieku. Wybierz inne.\n")
    print("Znakomicie...")
    return move

## SUPER COMPUTER MOVES 
## HERO NOT DEFEATED!

def computer_move(board, computer, human):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utworz kopie robocza, poniewaz funkcja bedzie zmieniac liste
    board = board[:]
    # najlepsze pozycje do zajecia wedlug kolejnosci
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end=" ")

    # jesli komputer moze wygrac, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY

    # jesli czlowiek moze wygrac, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # ten ruch zostal sprawdzony, wycofaj go
        board[move] = EMPTY

##

    # jesli plansza jest pusta, wez krawedz
    moves_left = len(legal_moves(board))
    if moves_left == 9:
        move = 7
        print(move)
        return move
    
    # jesli to drugi ruch, wez srodek jesli rog jest zajety
    # wez naroznik zaraz obok krawedzi, lub wez krawedz jesli srodek wziety

    elif moves_left == 8:
        if (0 not in legal_moves(board)) or (2 not in legal_moves(board)) or (6 not in legal_moves(board)) or (8 not in legal_moves(board)):
            move = 4
        elif (1 not in legal_moves(board)) or (3 not in legal_moves(board)):
            move = 0
        elif (5 not in legal_moves(board)) or (7 not in legal_moves(board)):
            move =8
        else:
            move = 0
        print(move)
        return move
    
    # jesli trzeci ruch, komputer wykonalby ruch na 7 a czlowiek wezmie kolejny
    elif moves_left == 7:
        if 4 not in legal_moves(board):
            move = 0
        else:
            move = 4
        print(move)
        return move
    
    # jesli czwarty ruch i srodek nie jest jeszcze wziety, wez go!
    # w przeciwnym razie, jesli oba rogi po przeciwnych stronach centralnego elementu zostalu zajete, wez strone.
    # w przeciwnym razie postepuj zgodnie z 'najlepszymi ruchami'
    elif moves_left == 6:
        if 4 in legal_moves(board):
            move = 4
            print(move)
            return move
        elif (0 not in legal_moves(board)) and (4 not in legal_moves(board)) \
             and (8 not in legal_moves(board)):
            move = 7
            print(move)
            return move
        elif (2 not in legal_moves(board)) and (4 not in legal_moves(board)) \
             and (6 not in legal_moves(board)):
            move = 1
            print(move)
            return move
        
    # jesli piaty ruch i czlowiek zrobil glupi ruch (wiec oni nie probuja wygrac)
    elif moves_left == 5:
        if (4 not in legal_moves(board)) and (1 not in legal_moves(board)):
            #uwaga, 7 i 0 nie beda w legal moves jesli komputer juz je wzial
            move = 6
        print('Uzywam piaty ruch')
        print(move)
        return move
    

    # poniewaz nikt nie moze wygrac w nastepnym ruchu, wybierz najlepsze wolne pole
    BEST_MOVES = (0, 2, 4, 6, 8, 1, 3, 5, 7)
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Zmien wykonawce ruchu."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """Pogratuluj zwyciezcy."""
    if the_winner != TIE:
        print(the_winner, "jest zwyciezca!\n")
    else:
        print("Remis!\n")

    if the_winner == computer:
        print("Jak przewidywalem, Czlowieku, jeszcze raz zostalem triumfatorem. \n" \
            "Dowod na to, ze komputery przewyzszaja ludzi pod kazdym wzgledem.")
                
    elif the_winner == human:
        print("No nie! To niemozliwe! Jakos udalo Ci sie mnie zwiesc, Czlowieku. \n" \
            "Ale to sie nigdy nie powtorzy! Ja, komputer, przyrzekam Ci to!")

    elif the_winner == TIE:
        print("Miales mnostwo szczescia, Czlowieku, i jakos udalo Ci sie ze mna " \
            "zremisowac. \nSwietuj ten dzien... bo to najlepszy wynik, jaki mozesz " \
            "kiekolwiek osiagnac.")

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
            
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

# rozpocznij program
main()

input("\n\nAby zakonczyc gre, nacisnij klawisz ENTER.")