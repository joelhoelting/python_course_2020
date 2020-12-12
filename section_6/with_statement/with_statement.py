import json

with open('friends.json', 'r') as file:
    file_contents = json.load(file)

print(file_contents)

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]
with open('cars.json', 'w') as file:
    json.dump(cars, file)
