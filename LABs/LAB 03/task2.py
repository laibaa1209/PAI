try:
    with open("task2.txt", "w") as file:
        file.write("betty bought a butter but the butter was bitter so betty bought another butter to make the bitter butter better.")
        file.close()

except:
    print("File Not Created")

file = open("task2.txt", "r")
try:
    data = file.read()
    data = data.replace("butter", "jam")
    file.close()

except :
    print("The word 'butter'doesn't exists in file ")


with open("task2.txt", "w") as file:
    file.write(data)

