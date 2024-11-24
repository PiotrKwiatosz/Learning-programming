# Rozdzial 7, Zadanie 3
# Gra zapisuje wyniki w pliku czysto tekstowym

import sys

##

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""

    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    points = next_line(the_file)
    
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, points, correct, explanation

def welcome(title):
    """Welcome the player"""
    print("Welcome to the game")
    print("The title of this session is:", title)

def high_scores(score):
    """Record's player's name and score if the score is high enough"""    
    high_score = open_file("high_scores1.txt", "r+")
    high_scores = []
    name = None
    win = score
    for i in range(5):
        score = high_score.readline()
        score = score.replace("\n","")
        name = high_score.readline()
        name = name.replace("\n","")
        score = int(score)
        high_scores.append((score, name))
    high_score.close()
    high_scores.sort()
    for scores in high_scores:
        scores = (score, name)
        if win > int(score): # only if got a high score does the score get entered
            name = input("You've got a high score! What's your name? ")
            print("Well done ", name, "! Your score is: ", win, "!", sep = "")
            high_scores.append((win, name))
            high_scores.pop(0)
            high_scores.sort(reverse = True) # ensure highscores in correct order
            high_score = open_file("high_scores1.txt", "w")
            for scores in high_scores:
                (score, name) = scores
                score = str(score)
                high_score.write(score)
                high_score.write('\n')
                high_score.writelines(name)
                high_score.write('\n')
            break
        else:
            print("Sorry, you didn't get a high score, better luck next time!")
    high_score.close()

def main():
    trivia_file = open_file("trivia_file2.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get the first block
    category, question, answers, points, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # get an answer
        answer = input("What's your answer?: ")
        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            points = int(points)
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
    

        # get next block
        category, question, answers, points, correct, explanation = next_block(trivia_file)

    high_scores(score)
    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

main()

##