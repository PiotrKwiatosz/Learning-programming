# Zadanie 02 ver. 1.6

# W pliku jest utrzymywana lista najlepszych wynikow. 
# Program rejestruje nazwe gracza i jego wynik, jesli miesci sie na liscie

import sys
from high_score import high_scores

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
    score_list = []
    for i in range(4):
        answers.append(next_line(the_file))
        try:
            score_list.append(int(next_line(the_file)))
        except:
            break
   
    explanation = next_line(the_file)

    return category, question, answers, score_list, explanation

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwe."""
    print("\t\tWitaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("kwiz3bkp.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # pobierz pierwszy blok
    category, question, answers, score_list, explanation = next_block(trivia_file)
    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedz
        answer = input("Jaka jest Twoja odpowiedz?: ")


        # przechowuj wyniki
        score = score + score_list[int(answer)-1]
        print(explanation)
        # pobierz kolejny blok
        category, question, answers, score_list, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To bylo ostatnie pytanie!")
    print("Twoj koncowy wynik wynosi", score)

    high_scores(score)

main()
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")