from addition import Addition


class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        new_sum = 0
        for i in range(1, num2 + 1):
            new_sum = cls.add(num1, new_sum)
        return new_sum

    @classmethod
    def divide(cls, num1, num2):
        counter = 0
        while num1 > 0:
            num1 = cls.add(num1, -num2)
            counter += 1
