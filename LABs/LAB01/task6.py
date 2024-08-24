physics_marks = float(input("enter physics marks: ")) #40
chemistry_marks = float(input("enter chemistry marks: ")) #78
math_marks = float(input("enter math marks: ")) #82

report = {
    "Physics": physics_marks,
    "Chemistry": chemistry_marks,
    "Math": math_marks 
}

total_sum = 0
count = 0
for key in report:
    total_sum+=report[key]
    count+=1

avg = total_sum/count
print("The average of her marks is: ", avg)

if(physics_marks > chemistry_marks and physics_marks > math_marks):
    print("Scored highest marks in physics")

elif(math_marks > chemistry_marks and math_marks > physics_marks):
    print("Scored highest marks in Maths")

else:
    print("Scored highest in chemistry")
    
