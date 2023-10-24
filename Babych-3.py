#3
#Write a program that will simulate user scores in a game. 
#Create a list with 5 players’ names after that simulate 100 rounds for each player. 
#As a result of the game create a list with the player's name and score (0-1000 range). 
#And save it to a CSV file.

import random

# Create a list of player names
players = ["Olena", "Serhiy", "Nicoline", "Jeppe", "Andrine"]

with open("game_results.csv", "w") as file:
    pass  

# Simulate 100 rounds for each player and write each round's score to CSV
for round in range(1, 101): 
    for name in players:
        score = random.randint(0, 1000)
        result_row = f"{name},{score}\n"
        with open("game_results.csv", "a") as f:
            f.write(result_row)

