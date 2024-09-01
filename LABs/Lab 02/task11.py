student_grades = {
    "Laiba": [89, 90, 76, 88],
    "Bilal": [89, 92, 98, 90],
    "Arwa":[82, 72, 88, 80],
    "Ramisha": [72, 82, 60, 70]
  
}

def add_grade(student_name, grade):
    if student_name in student_grades:
        student_grades[student_name].append(grade)
        print("Grade added!")
    else:
        print("Error! Grade not added")

def calculate_avg_grade(student_name):
    if student_name in student_grades:
        lst = list(student_grades[student_name])
        if len(lst) != 0:
            avg = sum(lst) / len(lst)
            print(f"The average marks of {student_name} is {avg}")
        else:
            print("DIvision by zero not possible.")
    else:
        print(f"The name {student_name} doesnot exist in the dictionary")

def add_student(new_student):
    student_grades[new_student] = []
    print(f"{new_student} added!")

def remove_student(student_name):
    if student_name in student_grades:
        del student_grades[student_name]
        print(f"{student_name} removed!")
    else:
        print(f"Error! No student with {student_name} found")

def main():
    add_grade("Bilal", 100)
    calculate_avg_grade("Laiba")
    add_student("Muzainah")
    remove_student("Ramisha")

main()
