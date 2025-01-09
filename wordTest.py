# This program tests if there are three consecutive letters in in alphabetical order in a word.


# First, I defined a function to test if there are consecutive letters in a word.
def consec_letters(user_word):
    # I set the initial condition of the result to be an empty string.
    result = ""

    # I started a loop that will be testing a letter of the word with the next letter, and the next letter
    # with the next next letter. I had the set the range of the position of the letters to be the length
    # of the word minus 2 so it would not pass a position that is not in the string.
    for pos in range(len(user_word) - 2):

        # This if statement compares the ASCII values of 3 letters. The first letter is the letter in the
        # position of the loop. Then, if 1 + the ASCII value of the first letter is equal to ASCII of the
        # second letter, the first statement is true. And, if 1 + the ASCII value of the second letter is equal
        # to the ASCII value of the third letter, the second statement is true. Both statements must be true, so
        # I used "and".
        if ord(user_word[pos])+1 == ord(user_word[pos+1]) and ord(user_word[pos+1])+1 == ord(user_word[pos+2]):
            result = "There are three consecutive letters in alphabetical order in the word "
            break

    # If the result string is still empty, the if statement was not used, therefore there are no consecutive
    # letters in the word.
    if result == "":
        result = "There are NO three consecutive letters in alphabetical order in the word "
    return result


# Define the main function.
def main():
    # Retrieve a word from the user.
    original_word = input("Input a word to check if there are three consecutive letters in it. ")
    # Save a lower case copy of the word to compare with ASCII values.
    test_word = original_word.lower()
    # If the word has less than 3 letters, print an error message.
    if len(test_word) < 3:
        print("The word has less than 3 letters.")

    # Print what the function returns with some fancy editing.
    else:
        print(consec_letters(test_word) + "'" + original_word + "'.")


if __name__ == "__main__":
    main()  
