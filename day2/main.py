rounds = []
scores = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3 # Scissors
}

wins = {
    "A": "C",
    "B": "A",
    "C": "B"
}

player_translate = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

player_translate_2 = {
    "X": lambda elf: wins[elf],
    "Y": lambda elf: elf,
    "Z": lambda elf: [move for move in scores.keys() if move not in [elf, wins[elf]]][0]
}

def score_process1(elf: str, player: str) -> int:
    player_pts = scores[player_translate[player]]

    if wins[player_translate[player]] == elf:
        # player win
        return player_pts + 6
    elif player_translate[player] == elf:
        # tie
        return player_pts + 3
    else:
        return player_pts

def score_process2(elf: str, player: str) -> int:
    player_move = player_translate_2[player](elf)
    
    player_pts = scores[player_move]

    if wins[player_move] == elf:
        # player win
        return player_pts + 6
    elif player_move == elf:
        # tie
        return player_pts + 3
    else:
        return player_pts

with open('day2.input', 'r') as file:
    rounds = file.read().split('\n')

rounds = list(filter(lambda x: x != '', rounds))
rounds = list(map(lambda x: x.split(' '), rounds))

round_scores = [score_process1(round_choice[0], round_choice[1]) for round_choice in rounds]
# print(round_scores)

total_points = sum(round_scores)

print("#1", total_points)

round_scores = [score_process2(round_choice[0], round_choice[1]) for round_choice in rounds]
# print(round_scores)

total_points = sum(round_scores)

print("#2", total_points)
