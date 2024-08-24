limit = int(input("Enter the total number of elements in the list: ")) #length of list

collection = []
print("enter list elements: ")

#input list
for i in range(limit):
    element = int(input())
    collection.append(element)

#number to comapre against
num = int(input("enter the number: "))

i = 0
while i < len(collection):
    if(collection[i] < num):
        del collection[i]
    else:
        i+=1

print(collection)