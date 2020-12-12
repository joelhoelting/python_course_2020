# numbers = [0, 1, 2, 3, 4]
# doubled_numbers = []
#
# # for number in numbers:
# #     doubled_numbers.append(number * 2)
#
# # Same way to do above
# doubled_numbers = [number * 2 for number in numbers]
#
# print(doubled_numbers)
#
# friend_ages = [22, 31, 35, 37]
# age_strings = [f"My friend is {age} years old " for age in friend_ages]
#
# print(age_strings)
#
# names = ["Rolf", "Bob", "Jen"]
# lowercase_names = [name.lower() for name in names]
# print(lowercase_names)

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [friend.lower() for friend in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")
