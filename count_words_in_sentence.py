# Ask the user to input a complete statement.
# Count the number of words in the input.

def count_words(sentence):
    # Counts the number of words in a sentence
    return len(sentence.split())

# Print the word count.
user_input = input("Enter a complete statement: ")
print("Output:", count_words(user_input))
