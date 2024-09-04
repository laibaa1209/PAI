import json

dict = {}
name = []
age = []
limit = int(input("Enter the limit length of list: "))

for i in range(limit):
    name_index = input("Enter your name: ")
    name.append(name_index)
    age_index = int(input("Enter your age: "))
    age.append(age_index)

    dict[name[i]] = age[i]

file_name = "json_file.json"

try:
    with open(file_name, 'w') as file:
        json.dump(dict, file, indent = 4)
    print(f"Data successfully saved to {file_name}.")
    with open(file_name, 'r') as file:
        data = json.load(file)
    print("Data successfully loaded from the JSON file:")
    print(data)
    max = 0
    for key, value in dict.items():
        if max < int(data[key]):
            max = int(data[key])
    for key, value in dict.items():
        if value == max:
            print(f"Maximum age is of {key}")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON in file '{file_name}'.")
except IOError as e:
    print(f"An IOError occurred: {e}")

