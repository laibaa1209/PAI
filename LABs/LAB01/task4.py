lists = []
for i in range(0, 5, 1):
    content = int(input("enter element: "))
    lists.append(content)
print(lists)

summ = 0
for i in range(0, 5):
    summ = summ + lists[i]
print("Sum: ", summ)
