def employee(name, salary):
    if(salary == 0):
        salary = 10000

    tax_amount = salary * (2 / 100)
    print("Name: ", name, "\nSalary after tax: ", tax_amount)
    
employee("laiba", 2300)