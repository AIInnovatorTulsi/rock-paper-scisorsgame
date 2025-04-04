import random

options = ("rock", "paper", "scissors")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
      player = input("Enter a choice (rock, paper, scissors):")

  print(f"Player: {player}")
  print(f"Computer: {computer}")

  if player == computer:
    print("MATCH TIE!")
  elif player == "rock" and computer == "scissors":
    print("YOU WIN!")
  elif player == "paper" and computer == "rock":
    print("YOU WIN!")
  elif player == "scissors" and computer == "paper":
    print("YOU WIN!")
  else:
    print("YOU LOSE!")

  play_again = input("Play again? (yes/no): ").lower()
  if not play_again == "y":
    running = False

print("Thanks for playing!")

