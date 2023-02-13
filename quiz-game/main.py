
def new_game():
    guesses = []
    correct_guesses = 0
    question_nom = 1
    for Key in questions:
        print("-----------------------------")
        print(Key)
        for i in options[question_nom - 1]:
            print(i)
        guess = input("Enter (A,B,C or C) ? ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(Key),guess)
        question_nom += 1
    display_score(correct_guesses, guesses)


#-----------------------------

def check_answer(answer, guess):
    if guess == answer:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#-----------------------------

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    print("Answers : ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Geusses : ",end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is : " + str(score) + "%")
    

#-----------------------------

def play_again():
    response = input("Do you want to play again ? (YES or NO) : ").upper()
    if response == "YES":
        return True
    else:
        return False

#-----------------------------

questions = {
    "Wo created Python ? ":"A",
    "What year was Python created ? ": "B",
    "Python is tributed to which comedy group ? ": "C",
    "Is the Earth round ? ": "A"}

options = [["A - Guido van Rossum","B - Elon Musk","C - Bill Gates","D - Mark Zuckerburg"],
          ["A - 1989","B - 1991","C - 2000","D - 2016"],
          ["A - Lonely Island","B - Smosh","C - MOnty Python","D - SNL"],
          ["A - True","B - False","C - Sometimes","D - What 's Earth ? "]]
new_game()
while play_again():
    new_game()
print("Byeeeee!")