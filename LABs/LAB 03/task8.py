try:
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    
    if val1 > 0:
        try:
            result = val2 / val1
            print(f"Division {val2} by {val1}: {result}")
        except ZeroDivisionError:
            print("ZeroDivisionError Occurred and Handled")
    else:
        print("First number must be greater than zero")

except ValueError:
    print("Value Error: Number input is not an integer")
