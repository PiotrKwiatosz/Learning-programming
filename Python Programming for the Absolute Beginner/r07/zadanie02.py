# Zadanie 02
# W pliku jest utrzymywana lista najlepszych wynikow. 
# Program rejestruje nazwe gracza i jego wynik jesli miesci sie na liscie

import sys

def open_file(file_name, mode):
    """Otworz plik."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie mozna otworzyc pliku", file_name, "Program zostanie zakonczony.\n", e)
        input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")
        sys.exit()
    else:
        return the_file
    
def next_line(the_file):
    """Zwroc kolejny wiersz pliku kwiz po sformatowaniu go."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Zwroc kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []

    for i in range (4):
        answers.append(next_line(the_file))

    points = next_line(the_file)

    correct = next_line(the_file)
    if correct:
        correct = correct[0]
   
    explanation = next_line(the_file)

    return category, question, answers, points, correct, explanation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwe."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def high_scores(score):
    import pickle, shelve
    """Zapisuje nazwe gracza i jego wynik jesli jest wystarczajaco duzy"""
    high_score = open("high_scores.dat", "rb")
    high_scores = pickle.load(high_score)
    high_score.close()
    high_scores.sort(reverse = True)
    win = score
    got_a_high_score = False
    for scores in high_scores:
        (score, name) = scores
