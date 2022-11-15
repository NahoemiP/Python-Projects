import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer":computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer: 
    return "It's a tie!!"
  elif player == "rock":
    if computer == "scissors":
      return "rock wins. You won!!."
    else:
      return "paper wins. You lose!"
  elif player == "paper":
    if computer == "scissors":
      return "scissors wins. You lose."
    else:
      return "rock wins. You lose!!"
  elif player == "scissors":
    if computer == "paper":
      return "scissors wins. You won!!."
    else:
      return "rock wins. You lose!"

choices = get_choices()
result  = check_win(choices["player"], choices["computer"])

print(result)