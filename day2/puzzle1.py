
hand = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS", 
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

beats = {
    "ROCK" : "SCISSORS",
    "PAPER" : "ROCK",
    "SCISSORS" : "PAPER",
}

hand_score = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}

with open('input.txt') as f:
    lines = f.readlines()

score = 0

for line in lines:
    values = line.split()
    opponent_throw = hand[values[0]]
    your_throw = hand[values[1]]
    score += hand_score[your_throw]
    winning_throw = beats[your_throw]
    if opponent_throw == your_throw:
        score += 3    
    elif opponent_throw == winning_throw:
        score += 6


print(score)