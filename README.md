


#1.Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.

X = 1
float_var = 1.0
str_var = '1'


print("Integer Variable:")
print("Value:", X)
print("Type:", type(X))

print("\nFloat Variable:")
print("Value:", float_var)
print("Type:", type(float_var))

print("\nString Variable:")
print("Value:", str_var)
print("Type:", type(str_var))

#2.Define a variable as Integer(2) ,Float(2.0) and String(‘2’) and print and return the value and type of variable.

y = 2
float_var = 2.0
str_var = '2'

print("Integer Variable:")
print("Value:", y)
print("Type:", type(y))

print("\nFloat Variable:")
print("Value:", float_var)
print("Type:", type(float_var))

print("\nString Variable:")
print("Value:", str_var)
print("Type:", type(str_var)




# Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c
a = b = c = 10


print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)



# Assign two variables a and b as integer and print the sum of a+b.

a = 5
b = 3


sum_ab = a + b
print("The sum of a and b is:", sum_ab)





# Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
fruits = ["apple", "banana", "cherry", "date", "elderberry"]


print("List of Fruits:")
print(fruits)

#How do you access the second and fourth elements from the list.

fruits = [f"apple", "banana", "cherry", "date", "elderberry"]
second_element = fruits[1]
print("Second element:", second_element)
fourth_element = fruits[3]
print("fourth element:", fourth_element)

#Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.

numbers = [10, 20, 30, 40, 50]
numbers[2] = 35
print(numbers)
[10, 20, 35, 40, 50]

colors = ("red", "green", "blue")
print(colors)


#Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.

 list_numbers = [10, 20, 30, 40, 50]
print(list_numbers)
list_numbers[2]=35
print(list_numbers)

#How do you create a tuple with the following elements: "red", "green", "blue"?


colors = ("red", "green", "blue", "yellow")
first_element = colors[0]
print(first_element)

#How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?

colors = ("red", "green", "blue", "yellow")
last_element = colors[-1]
print(last_element)

#What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?

colors = ("red", "green", "blue")
colors[1] = "yellow"  

#Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.

coordinates = (10, 20, 30)


x, y, z = coordinates

print("x =", x)
print("y =", y)
print("z =", z)

#Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").


colors = ("red", "green", "blue")


if "blue" in colors:
    print("The element 'blue' is present in the tuple.")
else:
    print("The element 'blue' is not present in the tuple.")
	
	
#Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
	
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")


length = len(days)

print("The length of the tuple is:", length)

#Create a dictionary where the keys are student names and the values are their grades. For example:
python
{"Alice": 85, "Bob": 90, "Charlie": 78} 

	
student_grades = {
    "John": 85 ,
    "Alice": 90,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

bob_grade = students["Bob"]

print("Bob's grade is:", bob_grade)	

#Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary
	
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["David"] = 92

del students["Charlie"]


#Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.	
	

	
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

students["Bob"] = 95

print("Updated students dictionary:", students)	



Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
if "Alice" in students:
    print("Yes, 'Alice' is a key in the dictionary.")
else:
    print("No, 'Alice' is not a key in the dictionary.")
	
	
#Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.	
	
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
num_pairs = len(students)
print("The number of key-value pairs in the dictionary is:", num_pairs)
