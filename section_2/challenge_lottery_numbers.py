import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))
print(lottery_numbers)

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

highest_number = 0
winning_player = None

for player in players:
    matching_numbers = len(lottery_numbers.intersection(player["numbers"]))
    if matching_numbers > highest_number:
        highest_number = matching_numbers
        winning_player = player["name"]

winnings = 100 ** highest_number

print("{winning_player} won {winnings}".format(winning_player=winning_player, winnings=winnings))
