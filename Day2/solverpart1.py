"""
Opponent will play:
A for Rock, B for Paper, and C for Scissors
I should play:
X for Rock, Y for Paper, and Z for Scissors

Score
X=1
Y=2
Z=3
Loss=0
Draw=3
Win=6
"""
score: int = 0
input_list = open(r"Day2/strategy_guide.txt", "r")

for line in input_list:
    opponent, response = line.split()
    # Score
    if response == "X":
        score = score + 1
        if opponent == "A":
            score = score + 3
        elif opponent == "B":
            score = score + 0
        elif opponent == "C":
            score = score + 6
    elif response == "Y":
        score = score + 2
        if opponent == "A":
            score = score + 6
        elif opponent == "B":
            score = score + 3
        elif opponent == "C":
            score = score + 0
    elif response == "Z":
        score = score + 3
        if opponent == "A":
            score = score + 0
        elif opponent == "B":
            score = score + 6
        elif opponent == "C":
            score = score + 3
print(score)
