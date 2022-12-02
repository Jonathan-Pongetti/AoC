
hand = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS", 
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

beats = {
    "ROCK" : "PAPER",
    "PAPER" : "SCISSORS",
    "SCISSORS" : "ROCK",
}
loses = {
    "SCISSORS" :"PAPER",
    "PAPER" :  "ROCK",
    "ROCK" : "SCISSORS",    
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
    outcome = hand[values[1]]
    #score += hand_score[your_throw]
    #winning_throw = beats[your_throw]
    if outcome == "DRAW":
        score += 3 
        score += hand_score[opponent_throw]   
    elif outcome == "WIN":
        score += 6
        score += hand_score[beats[opponent_throw]]
    elif outcome == "LOSE":
        score += hand_score[loses[opponent_throw]]

print(score)