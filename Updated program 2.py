#Ben Krehbiel
#4/1/2025
#vroom vroom


class Car:

    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0


    def accelerate(self):
        self.__speed += 5


    def slow(self):
        self.__speed -= 5


    def get_speed(self):
        return self.__speed


c1 = Car("2002", "ford explorer")

for i in range(5):
    c1.accelerate()
    print(c1.get_speed())
for i in range(5):
    c1.slow()
    print(c1.get_speed())
