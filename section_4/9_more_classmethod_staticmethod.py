class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, val1, val2):
        return cls(val1 + val2)


number = FixedFloat(18.757482)
new_number = FixedFloat.from_sum(12.32, 15.0131)
print(new_number)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f"<Dollar {self.symbol}{self.amount:.2f}>"


money = Dollar.from_sum(25.25, 23.22)
print(money)
