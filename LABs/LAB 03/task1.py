try:
    with open("task.txt", 'r') as file:
        data = file.read()

    print("The character count is:", len(data))

except FileNotFoundError:
    print("The file 'task.txt' was not found.")
