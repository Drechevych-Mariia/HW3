class Vehicles:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def describe(self):
        return f'max speed is {self.max_speed} and mileage is {self.mileage}'


class Bus(Vehicles):
    def __init__(self, seating_capacity, max_speed, milage):
        super(Bus, self).__init__(max_speed, milage)
        self._seating_capacity = seating_capacity

    def number_of_seats(self):
        return f'Bus has {self._seating_capacity}'


print(type(Bus))

print(issubclass(Bus, Vehicles))


class School_bus:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


print(issubclass(School_bus, Vehicles))


class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students


class SchoolBus(School, Bus):

    def __init__(self, school_id, max_speed, mileage, seating_capacity, bus_school_color, number_of_students):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def color(self):
        return f'Bus color {self.bus_school_color}'


class Bear:
    def make_sound(self):
        print('Brrrr')


class Wolf:
    def make_sound(self):
        print('Wwww')


bear = Bear()
wolf = Wolf()

animals = (bear, wolf)

for animals in (bear, wolf):
    animals.make_sound()


class City:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'The population of {self.name} is {self.population}.'


class Addition:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if self.value > 10 or other.value > 10:
            return self.value * other.value
        return self.value + other.value


class Sum:
    def __call__(self, number_1, number_2):
        return number_1 + number_2
sum_1 = Sum()

class MyOrder:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))

