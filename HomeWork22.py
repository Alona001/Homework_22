import random
you_win ="You win!"
you_lose ="You lose!"
choices = ["Stone", "Scissors", "Paper"]

random_item = random.choice(choices)
user_item = input("Enter your choice: Stone, Scissors or Paper: ")

if user_item == "Stone" and random_item == "Scissors":
    print(you_win)
if user_item == "Scissors" and random_item == "Stone":
    print(you_lose)
if user_item == "Scissors" and random_item == "Paper":
    print(you_win)
if user_item == "Paper" and random_item == "Scissors":
    print(you_lose)
if user_item == "Paper" and random_item == "Stone":
    print(you_win)
if user_item == "Stone" and random_item == "Paper":
    print(you_lose)
if user_item == random_item :
    print("Draw game")