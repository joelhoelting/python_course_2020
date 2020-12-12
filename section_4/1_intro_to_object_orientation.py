# student = {
#     'name': 'Rolf Smith',
#     'grades': [70, 88, 90, 99]
# }
#
#
# def student_avg(student):
#     student_grades = student['grades']
#     return sum(student_grades) / len(student_grades)
#
#
# print(student_avg(student))
#
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student_one = Student('Rolf Smith', [70, 88, 99])
# student_two = Student('Zane Rozco', [50, 60, 70, 80])
#
# print(student_one.__class__)

# # We've already defined a movie class like this:
# class Movie:
#     def __init__(self, new_name, new_director):
#         self.name = new_name
#         self.director = new_director
#
#     # let's try to add a method `print_info()` here:
#     def print_info(self):
#         print("{} by {}".format(self.name, self.director))
#
# matrix = Movie('Matrix', 'Wachowskis')
# matrix.print_info()