#practice task 1:
a = 8
b = 3

def addition():
    print(a + b)


def subtraction():
    print(a - b)


def multiplication():
    print(a * b)


def division():
    print(a / b)


addition()
subtraction()
multiplication()
division()

#practice task 2:
def print_greeting():
    print("Welcome User!")
    
print_greeting()

#practice task 3:
def calculate_rectangle_area(length, width):
    print("area of rectangle: ",length *width )
    
calculate_rectangle_area(2, 3)

#practice task 4:
def maximum_number(number):
    max = number[0]
    for i in range(1, len(number)):
        for j in range(1, len(number)): 
            if(max < number[i]):
                max = number[i]
    print("The maximum number is: ", max)
    
numbers = [1, 2, 3, 4, 5, 6]
maximum_number(numbers)

#lambda function(practice task 5):
multiplication = lambda x =2, y = 3, z = 1 : x*y*z
print(multiplication())

#STRING TASKS
#task 6:
name = input("Enter your good name: ")
titled_name = name.title()

if(titled_name.istitle()):
    print("Hello ", titled_name)
else:
    print("Name is not titled.")
    
ans = input("I hope you are fine, let me know how I can help you!: ")

if(ans == 'yes'):
    print("Share your problem with us: ")
    input()
    print("Thanks for your feedback, we will resolve your problem!")
else:
    string = "okay good to see you stay connected!"
    print(string.center(50))
    
#Task 7:
full_name = input("Enter your full name: ")
name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1]

print("First Name: ", first_name, "\nLast Name: ", last_name)