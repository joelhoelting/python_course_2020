# friends = ["Rolf", "Hannah", "Miley"]
#
# for friend in friends:
#     print(friend)

students = [
    {"name": "Rolf", "grade": 50},
    {"name": "Amanda", "grade": 60},
    {"name": "Hannah", "grade": 80},
    {"name": "Alpha", "grade": 22}
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print("{name} has a grade of {grade}".format(name=name, grade=grade))