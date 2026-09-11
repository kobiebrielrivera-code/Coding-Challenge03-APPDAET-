import random

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)

player = input("Enter your choice (rock, paper, or scissor): ")

if player == computer:
    print("Tie")

elif (player == "rock" and computer == "scissor") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissor" and computer == "paper"):
    print("Player Win")
else:
    print("Computer Win")


