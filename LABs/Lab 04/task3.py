# Make a class "Student"and make a function "Print_biodata" inside it. Pass name and age of
# student to constructor. Now access "Print_biodata" function using object to print name and age of student.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_biodata(self):
        print(f"Name: {self.name}\nAge: {self.age}")

def main():
    student = Student("Laiba", 19)
    student.print_biodata()

main()