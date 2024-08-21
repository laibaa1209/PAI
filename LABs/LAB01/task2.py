print("-----Calculator-----")
operation = int(input("Enter The Operation You Want To Perform: \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
val1 = int(input("Enter 1st value: "))
val2 = int(input("Enter 2nd value: "))

if operation == 1:
    print("sum: ", -(-val1 - val2))
elif operation == 2:
    print("subtraction: ", val1 - val2)
elif operation == 3:
    print("multiplication: ", val1 * val2)
else:
    print("division: ", val1/val2)






