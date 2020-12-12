class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


"""
However you can see there’s a lot of duplication between our `Student` and `WorkingStudent` classes. Instead, we may choose to make our `WorkingStudent` extend the `Student`. It keeps all the same functionality, but we can add more.
"""

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 40

rolf = WorkingStudent("Rolf", "MIT", 15.50)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.weekly_salary)