marks = float(input("Enter Your Marks: "))

if marks > 100:
    print("Invalid Marks")

if marks >= 80.0:
    print("you are enrolled in CS")
    if marks > 85:
        print("And your section is A")
    else:
        print("And your section is B")

elif marks >= 70.0:
    print("you are enrolled in AI")
    if marks > 75:
        print("And your section is A")
    else:
        print("And your section is B")

elif marks >= 60.0:
    print("you are enrolled in DS")
    if marks > 65:
        print("And your section is A")
    else:
        print("And your section is B")

else:
    print("You Have Failed!")