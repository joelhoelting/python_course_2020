# friend_ages = {"Rolf": 24, "Adam": 32, "Anne": 88, "Max": 33}
#
# print(friend_ages)
#
# friends = (
#     {"name": "Rolf Smith", "age": 24},
#     {"name": "Adam Wool", "age": 33},
#     {"name": "Anne Pun", "age": 19}
# )
#
# print(friends[0]["name"])

friends = [("Rolf", 24), ("Adam", 32), ("Anne", 88), ("Max", 33)]
friend_ages = dict(friends)
print(friend_ages)
