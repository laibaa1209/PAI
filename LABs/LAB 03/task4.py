try:

    name = input("Enter your name: ")
    CNIC = input("Enter your CNIC: ")
    age = int(input("Enter your age: "))
    salary = float(input("Enter your salary: "))
    
    with open("task4.txt", "w") as file:
        file.write(f"Name: {name} \nCNIC: {CNIC} \nAge: {age} \nSalary: {salary}\n")
    
    phone_number = input("Enter your phone number: ")
    with open("task4.txt", "a") as file:
        file.write(f"Phone Number: {phone_number}\n")
    
    with open("task4.txt", "r") as file:
        data = file.read()
    
    print("The content of the file:\n", data)

except ValueError:
    print("Please enter valid data.")
except FileNotFoundError:
    print("The file could not be found.")


