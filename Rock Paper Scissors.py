import random
choices = {"R":"Rock", "P":"Paper", "S":"Scissors"}
from colorama import Fore, init

init(autoreset=True)



def score_shower(comp_score, play_score):
    computer_score = comp_score
    player_score = play_score
    print(f"Player score: {player_score}. \nComputer score: {computer_score}")

def game(comp_score, play_score):
    computer = random.choice(list(choices.values()))
    computer_score = comp_score
    player_score = play_score
    while True:
        print(Fore.RED + "Rock (R), Paper (P), or Scissors (S)?")
        choice = input().upper()
        if choice == "R":
            player = choices[str(choice)]
            break
        elif choice == "P":
            player = choices[str(choice)]
            break
        elif choice == "S":
            player = choices[str(choice)]
            break
        else:
            print("Please put in valid input")
            continue

    if player == computer:
        print("Computer: ", computer)
        print("Player: ",player)
        print("Tie!")
        score_shower(computer_score, player_score)

    elif player == "Rock":
        if computer == "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost")
            computer_score += 1
            score_shower(computer_score, player_score)
        if computer == "Scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You won")
            player_score += 1
            score_shower(computer_score, player_score)
    elif player == "Paper":
        if computer == "Scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost")
            computer_score += 1
            score_shower(computer_score, player_score)
        if computer == "Rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You won")
            player_score += 1
            score_shower(computer_score, player_score)
    elif player == "Scissors":
        if computer == "Rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lost")
            computer_score += 1
            score_shower(computer_score, player_score)
        if computer == "Paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You won")
            player_score += 1
            score_shower(computer_score, player_score)

    play_again = input("Play again? (Y/N): ").upper()

    if play_again == "Y":
        game(computer_score, player_score)
    else:
        score_shower(computer_score, player_score)
        print("See you next time!")
        
if __name__ == "__main__":
    comp_score = 0
    play_score = 0
    game(comp_score, play_score)
        