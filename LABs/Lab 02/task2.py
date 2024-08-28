def check_vowel_constant(word):
    vowels = 'aeiou'
    char = word[- 1]

    for i in range(len(vowels)):
        if(char == vowels[i]):
            print("It is a vowel")
            break
        else:
            print("It is a constant")
            break

def main():
    word = input("Enter a string: ")
    check_vowel_constant(word)
    
main()

