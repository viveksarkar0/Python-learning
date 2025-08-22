# ===============================
# 🏗️ PYTHON OBJECT-ORIENTED PROGRAMMING
# ===============================

# ===============================
# 📚 CLASSES AND OBJECTS
# ===============================

class Person:
    """A simple class to represent a person"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Constructor method - called when creating a new object"""
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def greet(self):
        """Instance method"""
        return f"Hello, my name is {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        """Method that modifies instance variable"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old"
    
    @classmethod
    def create_anonymous(cls):
        """Class method - creates a person with default values"""
        return cls("Anonymous", 0)
    
    @staticmethod
    def is_adult(age):
        """Static method - doesn't need instance or class"""
        return age >= 18
    
    def __str__(self):
        """String representation of the object"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):
        """Detailed string representation for debugging"""
        return f"Person('{self.name}', {self.age})"

# Creating objects (instances)
person1 = Person("Vivek", 22)
person2 = Person("Alice", 25)

print(person1.greet())  # Hello, my name is Vivek and I'm 22 years old
print(person2.greet())  # Hello, my name is Alice and I'm 25 years old

# Accessing instance variables
print(person1.name)  # Vivek
print(person1.age)   # 22

# Accessing class variables
print(Person.species)  # Homo sapiens
print(person1.species) # Homo sapiens

# Using instance methods
print(person1.have_birthday())  # Happy birthday! Vivek is now 23 years old

# Using class method
anonymous = Person.create_anonymous()
print(anonymous)  # Person(name='Anonymous', age=0)

# Using static method
print(Person.is_adult(20))  # True
print(Person.is_adult(16))  # False

# String representations
print(str(person1))   # Person(name='Vivek', age=23)
print(repr(person1))  # Person('Vivek', 23)

# ===============================
# 🔒 ENCAPSULATION
# ===============================

class BankAccount:
    """Example of encapsulation with private attributes"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance  # Protected attribute (convention)
        self.__account_number = self._generate_account_number()  # Private attribute
    
    def _generate_account_number(self):
        """Private method to generate account number"""
        import random
        return f"ACC{random.randint(10000, 99999)}"
    
    def get_balance(self):
        """Public method to get balance"""
        return self._balance
    
    def deposit(self, amount):
        """Public method to deposit money"""
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid amount"
    
    def withdraw(self, amount):
        """Public method to withdraw money"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_account_info(self):
        """Public method to get account information"""
        return {
            "holder": self.account_holder,
            "balance": self._balance,
            "account_number": self.__account_number
        }

# Using the BankAccount class
account = BankAccount("Vivek", 1000)
print(account.deposit(500))   # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300
print(account.get_balance())  # 1300

# Accessing protected attribute (works but not recommended)
print(account._balance)  # 1300

# Accessing private attribute (will raise AttributeError)
# print(account.__account_number)  # AttributeError

# ===============================
# 🧬 INHERITANCE
# ===============================

class Animal:
    """Base class (parent class)"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some animal sound"
    
    def get_info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Derived class (child class) - inherits from Animal"""
    
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override parent method"""
        return "Woof! Woof!"
    
    def fetch(self):
        """New method specific to Dog"""
        return f"{self.name} is fetching the ball"
    
    def get_info(self):
        """Override parent method with additional info"""
        return f"{super().get_info()} of breed {self.breed}"

class Cat(Animal):
    """Another derived class"""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        return "Meow! Meow!"
    
    def climb(self):
        return f"{self.name} is climbing the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.get_info())      # Buddy is a Dog of breed Golden Retriever
print(cat.get_info())      # Whiskers is a Cat
print(dog.make_sound())    # Woof! Woof!
print(cat.make_sound())    # Meow! Meow!
print(dog.fetch())         # Buddy is fetching the ball
print(cat.climb())         # Whiskers is climbing the tree

# ===============================
# 🔄 POLYMORPHISM
# ===============================

def animal_sound(animal):
    """Function that works with any animal (polymorphism)"""
    return animal.make_sound()

# Same function works with different animal types
animals = [dog, cat]
for animal in animals:
    print(f"{animal.name}: {animal_sound(animal)}")

# ===============================
# 📦 ABSTRACTION
# ===============================

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def area(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def describe(self):
        """Concrete method - can be used by all subclasses"""
        return f"This shape has area {self.area()} and perimeter {self.perimeter()}"

class Rectangle(Shape):
    """Concrete class implementing Shape"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Another concrete class implementing Shape"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Using abstract classes
shapes = [
    Rectangle(5, 3),
    Circle(4)
]

for shape in shapes:
    print(shape.describe())

# ===============================
# 🎯 SPECIAL METHODS (MAGIC METHODS)
# ===============================

class Vector:
    """Example class with special methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Vector addition"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Vector subtraction"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Vector multiplication by scalar"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality comparison"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Length of vector (magnitude)"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

# Using special methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)                    # Vector(3, 4)
print(v1 + v2)              # Vector(4, 6)
print(v1 - v2)              # Vector(2, 2)
print(v1 * 2)               # Vector(6, 8)
print(v1 == v2)             # False
print(len(v1))              # 5 (magnitude)

# ===============================
# 🏭 FACTORY PATTERN
# ===============================

class AnimalFactory:
    """Factory class to create different types of animals"""
    
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        """Factory method to create animals"""
        if animal_type.lower() == "dog":
            return Dog(name, kwargs.get("breed", "Unknown"))
        elif animal_type.lower() == "cat":
            return Cat(name, kwargs.get("color", "Unknown"))
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Using factory pattern
factory = AnimalFactory()
my_dog = factory.create_animal("dog", "Max", breed="Labrador")
my_cat = factory.create_animal("cat", "Luna", color="Black")

print(my_dog.get_info())  # Max is a Dog of breed Labrador
print(my_cat.get_info())  # Luna is a Cat

# ===============================
# 🎯 PRACTICAL EXAMPLE: STUDENT MANAGEMENT SYSTEM
# ===============================

class Student:
    """Student class for management system"""
    
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.grades = {}
    
    def enroll_course(self, course):
        """Enroll in a course"""
        if course not in self.courses:
            self.courses.append(course)
            return f"{self.name} enrolled in {course}"
        return f"{self.name} is already enrolled in {course}"
    
    def add_grade(self, course, grade):
        """Add grade for a course"""
        if course in self.courses:
            self.grades[course] = grade
            return f"Grade {grade} added for {course}"
        return f"{self.name} is not enrolled in {course}"
    
    def get_gpa(self):
        """Calculate GPA"""
        if not self.grades:
            return 0.0
        
        total_points = sum(self.grades.values())
        return total_points / len(self.grades)
    
    def __str__(self):
        return f"Student(ID: {self.student_id}, Name: {self.name}, GPA: {self.get_gpa():.2f})"

class StudentManager:
    """Manager class to handle multiple students"""
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        """Add a student to the system"""
        self.students[student.student_id] = student
        return f"Student {student.name} added successfully"
    
    def get_student(self, student_id):
        """Get student by ID"""
        return self.students.get(student_id)
    
    def list_students(self):
        """List all students"""
        return [str(student) for student in self.students.values()]
    
    def get_top_students(self, n=3):
        """Get top n students by GPA"""
        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.get_gpa(),
            reverse=True
        )
        return sorted_students[:n]

# Using the student management system
manager = StudentManager()

# Create students
student1 = Student("S001", "Vivek", 22)
student2 = Student("S002", "Alice", 20)
student3 = Student("S003", "Bob", 21)

# Add students to manager
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

# Enroll students in courses
student1.enroll_course("Python Programming")
student1.enroll_course("Data Structures")
student2.enroll_course("Python Programming")
student3.enroll_course("Web Development")

# Add grades
student1.add_grade("Python Programming", 95)
student1.add_grade("Data Structures", 88)
student2.add_grade("Python Programming", 92)
student3.add_grade("Web Development", 85)

# Display results
print("All Students:")
for student in manager.list_students():
    print(f"  {student}")

print("\nTop Students:")
for student in manager.get_top_students(2):
    print(f"  {student}")

# ===============================
# END OF OBJECT-ORIENTED PROGRAMMING
# ===============================
