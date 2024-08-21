lists = []
for i in range(0, 5, 1):
    content = int(input("enter element: "))
    lists.append(content)
print(lists)

count = 0
for i in range(0, 5):
    if lists[i] % 2 == 0:
        count = count + 1
print(count)
