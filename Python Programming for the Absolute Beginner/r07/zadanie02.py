# Zadanie 02
# W pliku jest utrzymywana lista najlepszych wynikow. 
# Program rejestruje nazwe gracza i jego wynik, jesli miesci sie na liscie

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

def high_scores(score):
    import pickle, shelve
    """Zapisuje nazwe gracza i jego wynik jesli jest wystarczajaco duzy"""
    print("Zapisywanie wysokich wynikow")

    win = score

    for scores in high_scores:
        (score, name) = scores
        if win >= int(score):
            got_a_high_score = True
            name = input("Zdobyles wysoki wynik! Jak sie nazywasz?")
            print("Dobra robota ", name, "! Twoj wynik to: ", win, "!", sep = "")
            high_scores.sort()
            high_scores.pop(0)
            high_scores.append((win, name))
            high_scores.sort(reverse = True)
            high_scores = open("high_scores_pickle.dat", "wb")
            pickle.dump(high_scores, high_score)
            break
    if got_a_high_score == False:
        print("Przepraszam, nie zdobyles dostatecznie wysokiego wynikum probuj jeszcze raz!")

    f = open("high_scores_pickle.dat", "wb")
    high_score = open_file("high_scores_pickle.dat", "rb")
    high_scores = pickle.load(high_scores)
    high_score.close()
    high_scores.sort(reverse = True)
    got_a_high_score = False
    high_score.close()

def welcome(title):
    """Przywitaj gracza i pobierz jego nazwe."""
    print("\t\t Witaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("kwiz2.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # pobierz pierwszy blok
    category, question, answers, points, correct, explanation = next_block(trivia_file)

    while category:
        # zadaj pytanie
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # uzyskaj odpowiedz
        answer = input("Jaka jest Twoja odpowiedz?: ")

        # sprawdz odpowiedz
        if answer == correct:
            print("\nOdpowiedz prawidlowa!", end=" ")
            points = int(points)
            score += points
        else:
            print("\n Odpowiedz niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")

        # pobierz kolejny blok
        category, question, answers, points, correct, explanation = next_block(trivia_file)

    high_scores(score)

    trivia_file.close()

    print("To bylo ostatnie pytanie!")
    print("Twoj koncowy wynik wynosi", score)

main()
input("\n\nAby zakonczyc program, nacisnij klawisz ENTER") 