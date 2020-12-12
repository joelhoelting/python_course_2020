class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Rolf Smith', [70, 88, 99])
student_two = Student('Zane Rozco', [50, 60, 70, 80])

print(Student.average(student_one))
print(student_one.average())