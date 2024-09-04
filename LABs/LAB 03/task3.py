length = int(input("Enter total number of elements of list 1 and 2(should be same): "))
lst1 = []
lst2 = []
dict = {}

for i in range(length):
    lst1.append(int(input(f"Enter element {i+1} of list 1: ")))
    lst2.append(int(input(f"Enter element {i+1} of list 2: ")))

    dict[lst1[i]] = lst2[i]

print(dict)

with open("task3.txt", "w") as file:
    file.write(str(dict))
