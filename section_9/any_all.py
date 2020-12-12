friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    },
]

# your_location = input('Where are you now? ')
# friends_nearby = [friend for friend in friends if friend['location'] == your_location]
# print(friends_nearby)
#
# if any(friends_nearby):
#     print('You are not alone')

print(all([1, 2, 3, 4]))  # --> True
print(all([0, 1, 2, 3, 4]))  # --> False
