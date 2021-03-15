class Laptop:
    def __init__(self, laptop_model, battery_power):
        self.battery_power = Battery(battery_power)
        self.laptop_model = laptop_model

    def __str__(self):
        return f"Лептоп {self.laptop_model} має {self.battery_power}"


class Battery:
    def __init__(self, battery_power):
        self.battery_power = battery_power

    def __str__(self):
        return f"Батарейку з зарядом {self.battery_power}"


battery = Laptop("Acer", "70%")
print(battery)


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitarstring = GuitarString()
guitar = Guitar(guitarstring)


class Calc:
    @staticmethod
    def __add_nums__(a, b, c):
        return a + b + c


print(Calc.__add_nums__(1, 2, 3))


class Pasta:
    def __init__(self, list):
        self.list = list

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


class Concert:
    max_visitor_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors < self.max_visitor_num:
            self._visitors_count = visitors
        else:
            self._visitors_count = self.max_visitor_num


Concert.max_visitor_num = 900
concert = Concert()
concert.visitors_count = 1500
print(concert.visitors_count)



import dataclasses


@dataclasses.dataclass()

class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int
import collections

AddressBookDataClass = collections.namedtuple('AdressBookDataClass',['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return (f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number},address={self.address},' \
            f' email={self.email}, birthday={self.birthday}, age={self.age})')

class Person:
    name = "John"
    age = 36
    country = "USA"

person = Person()
setattr(person, "age", 3)
print(person.age)


class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

mary = Student(30, 'Mary')

setattr(mary, 'student_email', 'student30@gmail.com')
print(getattr(mary, 'student_email'))


class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def conv(self):
        return ((self._temperature * 1.8) + 32)

celsius = Celsius(100)
print(f'{celsius.conv}')