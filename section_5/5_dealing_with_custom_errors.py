class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but can only add `Car` objects.')
        self.cars.append(car)


ford_garage = Garage()

car = Car('Ford', 'Fiesta')

try:
    ford_garage.add_car(car)
except TypeError:
    print("Your car was not a Car!")
except ValueError:
    print("Something weird happened")
finally:
    print(f"The garage now has {len(ford_garage)} cars")