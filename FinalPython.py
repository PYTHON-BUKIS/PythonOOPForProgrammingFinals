#just to remind myself this is the Vehicle class
class Vehicle:
    def __init__(self, busname, model):
        self.busname = busname
        self.model = model

class Bus(Vehicle):
    pass

class SchoolBus(Bus):
    pass

school_bus = SchoolBus("Twin Coach", "Model 40")
print(isinstance(school_bus, Vehicle))
print(f"Bus Name: {school_bus.busname} || Model: {school_bus.model}")

#Employee Class Agagaga
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, employee_str):
        name, age = employee_str.split('-')
        return cls(name, int(age))

employ1 = Employee("Alessandro", 38)
employ2 = Employee.from_string("Fallore-46")
print(" ")
print(employ1.name, employ1.age)
print(employ2.name, employ2.age)

#School and Students Lmao
class School:
    def __init__(self, students):
        self.students = students

    def average_grade(self):
        total = sum(student['grade'] for student in self.students)
        return total / len(self.students)
    
    def average_gpa(self):
        total = sum(student['gpa'] for student in self.students)
        return total / len(self.students)

class SchoolOne(School):
    pass

class SchoolTwo(School):
    pass

students_one = [
    {'name': 'Cyrano', 'grade': 98, 'gpa': 4.0},
    {'name': 'Helmi', 'grade': 89, 'gpa': 3.3},
]

students_two = [
    {'name': 'Luciano', 'grade': 96, 'gpa': 4.0},
    {'name': 'Anastasios', 'grade': 86, 'gpa': 3.3},
]

school_one = SchoolOne(students_one)
school_two = SchoolTwo(students_two)

print(" ")
print(school_one.average_grade())
print(school_one.average_gpa())
print(school_two.average_grade())
print(school_two.average_gpa())

#VECTORS I THOUGH I WAS FREE FROM LINEAR >:(
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(5, 8)
v2 = Vector(3, 7)
v3 = v1 + v2

print(" ")
print(v3)

#Book AND Authors
class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author.name}"

author = Author("Harper Lee")
book = Book("To Kill a Mockingbird", author)

print(" ")
print(book)
