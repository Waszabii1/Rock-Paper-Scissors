import random
while True:
    choices = ["Rock", "Paper", "Scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper, or Scissors?: ").capitalize()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "Rock" and computer != "Rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost :(")
    elif player == "Scissors" and computer != "Scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost :(")
    elif player == "Paper" and computer != "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win! :)")

    play_again = input("Play again? (Y/N): ").upper()

    if play_again != "Y":
        break
