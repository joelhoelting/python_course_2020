lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {
        'name': 'James',
        'numbers': {1, 2, 3, 6, 8}
    },
    {
        'name': 'Sally',
        'numbers': {1, 3, 8, 22, 18}
    }
]

james_numbers = players[0]["numbers"]
james_numbers_correct = len(lottery_numbers.intersection(james_numbers))

sally_numbers = players[1]["numbers"]
sally_numbers_correct = len(lottery_numbers.intersection(sally_numbers))

print(f"James got {james_numbers_correct} numbers correct")
print("Sally got {sally_numbers_correct} numbers correct".format(sally_numbers_correct=sally_numbers_correct))
