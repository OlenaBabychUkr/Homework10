import csv

# Read data from the CSV file
player_scores = {}
with open("game_results.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        name, score = row[0], int(row[1])
        if name not in player_scores:
            player_scores[name] = 0
        player_scores[name] = max(player_scores[name], score)

# Sort player scores by descending order
sorted_scores = sorted(player_scores.items(), key=lambda x: x[1], reverse=True)

# Write high scores to a new CSV file
with open("high_scores.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Player", "Highest Score"])
    for name, score in sorted_scores:
        writer.writerow([name, score])
