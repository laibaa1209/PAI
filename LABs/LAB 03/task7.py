def replacement_neeeded(file_name) :
    with open(file_name, "w") as file:
        file.write("that is an jpple")
    
    with open(file_name, "r") as file:
        data = file.read()

        try:
            data = data.replace("j", "a")
        except:
            print("The letter doesn't exist")

    try:
        with open(file_name, "w") as file:
            file.write(data)
    except FileNotFoundError:
        print("File doesn't exist")

def main() :
    replacement_neeeded("replacement_nedded.txt")

main()