import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors : ").lower()
    print("computer : ",computer.capitalize())
    print("player : ",player.capitalize())
    if player == computer:
        print("Tie!")
    elif player == choices[0]:
        if computer == choices[1]:
            print("You lose!")
        elif computer == choices[2]:
            print("You win!")
    elif player == choices[1]:
        if computer == choices[0]:
            print("You win!")
        elif computer == choices[2]:
            print("You lose!")
    else:
        if computer == choices[0]:
            print("You lose!")
        elif computer == choices[1]:
            print("You win!")
    play_again = input("Play again ? (YES or NO) : ").lower()
    if play_again !="yes":
        break
print("Bay!")
