#Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
#To each file append a random number between 1 and 100. 
#Create a summary file (summary.txt) that contains the name of the file and the number in that file: A.txt: 67 B.txt: 12...Z.txt: 98

import random

# Generate and write random numbers to individual files
for letter in range(65, 91):
    filename = chr(letter) + ".txt"
    with open(filename, "w") as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number))

# Create summary file with file names and corresponding random numbers
with open("summary.txt", "w") as summary_file:
    for letter in range(65, 91):
        filename = chr(letter) + ".txt"
        with open(filename, "r") as f:
            random_number = f.read()
        summary_file.write(f"{filename}: {random_number}\n")
