"""
Opponent will play:
A for Rock, B for Paper, and C for Scissors
I should play:
X for Rock, Y for Paper, and Z for Scissors
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
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

win_points = 6
draw_points = 3
loss_points = 0


class GamePiece:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.beats = None
        self.loses = None


rock = GamePiece("Rock", 1)
paper = GamePiece("Paper", 2)
scissors = GamePiece("Scissors", 3)

rock.beats = scissors
paper.beats = rock
scissors.beats = paper
rock.loses = paper
paper.loses = scissors
scissors.loses = rock

opponent: str = ""
outcome: str = ""
opponent_throw: GamePiece


for line in input_list:
    opponent, outcome = line.split()
    if opponent == "A":
        opponent_throw = rock
    elif opponent == "B":
        opponent_throw = paper
    elif opponent == "C":
        opponent_throw = scissors
    else:
        print("Error")
    # win
    if outcome == "Z":
        score = score + win_points
        score = score + opponent_throw.loses.value

    # draw
    elif outcome == "Y":
        score = score + draw_points
        score = score + opponent_throw.value

    # loss
    elif outcome == "X":
        score = score + loss_points
        score = score + opponent_throw.beats.value
    else:
        print("Error")

print(score)
