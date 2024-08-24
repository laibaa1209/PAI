word = input("Enter a word: ")

reversed_word = ""

for i in range(len(word)):
    reversed_word += word[len(word) - 1 - i]

print("The reversed word is: ", reversed_word)
