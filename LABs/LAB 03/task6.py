sentence = input("Enter The Sentence: ")

with open("question.txt", "w") as file:
    try:
        if(sentence[len(sentence)-1] == "?"):
            file.write(sentence)

    except ValueError:
        print("Value Error: sentence entered is not a question.")