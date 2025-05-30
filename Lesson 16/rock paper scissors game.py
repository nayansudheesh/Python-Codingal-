import random

options = ["paper" , "scissor" , "rock"]
computer_choice = random.choice(options)
player_choice = input("Choose from paper scissor and rock to beat computer.(must have no capitals)")

print("players(your) choice is" , player_choice)
print("Computers choice is", computer_choice)

if player_choice == computer_choice:
    print("It is a tie, try again.")
elif player_choice == "paper" and computer_choice == "rock":
    print("Paper beats rock, you have won!")
elif player_choice == "rock" and computer_choice == "scissor":
    print("rock smashes scissor, you have won!")
elif player_choice == "scissor" and computer_choice == "paper":
    print("Scissor cuts paper, you have won!")
else:
    print("You have lost, try again.")