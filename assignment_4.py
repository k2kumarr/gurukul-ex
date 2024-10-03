

1. Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# Define the Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Display the details of the car
print("Car Details:")
my_car.display_details()



2. Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Student Details:\nName: {self.name}\nRoll Number: {self.roll_number}\nMarks: {self.marks}")

# Create an object of the Student class
student1 = Student("Alice", 101, 95)

# Display the student's information
student1.display_info()

3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?

# Define the Rectangle class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

# Create multiple objects of the Rectangle class
rectangle1 = Rectangle(5, 7)
rectangle2 = Rectangle(10, 12)
rectangle3 = Rectangle(15, 20)

# Display the area and perimeter for each rectangle
print("Rectangle 1:")
print(f"Area: {rectangle1.calculate_area()}")
print(f"Perimeter: {rectangle1.calculate_perimeter()}")

print("\nRectangle 2:")
print(f"Area: {rectangle2.calculate_area()}")
print(f"Perimeter: {rectangle2.calculate_perimeter()}")

print("\nRectangle 3:")
print(f"Area: {rectangle3.calculate_area()}")
print(f"Perimeter: {rectangle3.calculate_perimeter()}")



4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?

# Import the math module for pi and pow functions
import math

# Define the Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius

# Create an object of the Circle class
circle = Circle(5)

# Display the area and circumference of the circle
print("Circle Details:")
print(f"Radius: {circle.radius}")
print(f"Area: {circle.get_area():.2f}")
print(f"Circumference: {circle.get_circumference():.2f}")



5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.


# Define the Account class
class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"Account {self.account_no} credited with ${amount:.2f}. New balance: ${self.balance:.2f}")

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Account {self.account_no} debited with ${amount:.2f}. New balance: ${self.balance:.2f}")

    def print_balance(self):
        print(f"Account {self.account_no} balance: ${self.balance:.2f}")

# Create an object of the Account class
account = Account("1234567890", 1000)

# Perform transactions
account.print_balance()
account.credit(500)
account.debit(200)
account.debit(1500)  # Insufficient balance!
account.print_balance()


6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.




# Define the Employee class
class Employee:
    employee_count = 0  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.increment_employee_count()  # Call the class method

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1  # Increment the class variable

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count  # Return the class variable

# Create new employee objects
print("Initial Employee Count:", Employee.get_employee_count())
emp1 = Employee("John Doe", 30)
print("Employee Count after creating emp1:", Employee.get_employee_count())
emp2 = Employee("Jane Doe", 25)
print("Employee Count after creating emp2:", Employee.get_employee_count())
emp3 = Employee("Bob Smith", 40)
print("Employee Count after creating emp3:", Employee.get_employee_count())

# Print employee details
print("\nEmployee Details:")
print(f"Name: {emp1.name}, Age: {emp1.age}")
print(f"Name: {emp2.name}, Age: {emp2.age}")
print(f"Name: {emp3.name}, Age: {emp3.age}")


7. Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.


# Define the Book class
class Book:
    def __init__(self, title, author, price=None):
        self.title = title
        self.author = author
        self.price = price if price is not None else 19.99  # Default price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

# Create book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 15.99)
book2 = Book("1984", "George Orwell")

# Display book details
print("Book 1 Details:")
book1.display_details()
print("\nBook 2 Details:")
book2.display_details()


8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.

# Define the TemperatureConverter class
class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Create a TemperatureConverter object
converter = TemperatureConverter()

# Convert various temperatures
print("Converting temperatures:")
print(f"25°C is equal to {converter.celsius_to_fahrenheit(25)}°F")
print(f"30°C is equal to {converter.celsius_to_fahrenheit(30)}°F")
print(f"35°C is equal to {converter.celsius_to_fahrenheit(35)}°F")



9. Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.

# Define the Time class
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        total_hours = self.hours + other_time.hours + total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours} hours and {self.minutes} minutes"

# Create Time objects
time1 = Time(5, 30)
time2 = Time(2, 45)

# Add time
time3 = time1.add_time(time2)

# Print time
print("Time 1:", time1)
print("Time 2:", time2)
print("Time 1 + Time 2 =", time3)


10.Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
