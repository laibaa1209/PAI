english_marks = float(input("enter english marks: ")) 
programming_marks = float(input("enter programming marks: ")) 
computer_marks = float(input("enter computer marks: ")) 
total_marks = float(input("Enter total marks of 3 subjects: "))

marks = {
    "English": english_marks,
    "Programming": programming_marks,
    "Computer": computer_marks 
}

total_subjects = len(marks)
obtained_marks = 0

for key in marks:
    obtained_marks += marks[key]


avg = obtained_marks / total_subjects 
print("The average of the marks is: ", avg)

perentage = (obtained_marks / total_marks) * 100
print("The percentage is: ",perentage)