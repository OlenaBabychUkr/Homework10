#3
#Write a program that will simulate user scores in a game. 
#Create a list with 5 players’ names after that simulate 100 rounds for each player. 
#As a result of the game create a list with the player's name and score (0-1000 range). 
#And save it to a CSV file.

import random

# Create a list of player names
players = ["Olena", "Serhiy", "Nicoline", "Jeppe", "Andrine"]

# Simulate 100 rounds for each player and store scores in a dictionary
players_scores = dict()
for name in players:
    score = 0
    for _ in range(100):
        score += random.randint(0, 10)
        players_scores[name] = score

# Create a list of player name and score pairs
results = []
for name, score in players_scores.items():
    results.append([name, score])

# Save the player results to a CSV file
with open("game_results.csv", "w") as f:
    for result in results:
        name, score = result
        f.write(f"{name},{score}\n")
