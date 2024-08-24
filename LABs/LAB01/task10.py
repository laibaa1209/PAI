limit = int(input("Enter the total number of elements in the list: ")) #length of list

collection = []
print("enter list elements: ")

#input list
for i in range(limit):
    element = int(input())
    collection.append(element)

max_element = collection[0]
for i in range(limit):
    if collection[i] > max_element:
            max_element = collection[i]
        
print("The maximum number in the list is: ", max_element)
