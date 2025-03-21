# Ask the user to input their full name.
# Count the number of characters excluding spaces.

def count_characters(name):
    # Counts the number of characters excluding spaces
    return len(name.replace(" ", ""))

# Print the character count.
user_input = input("Enter your full name: ")
print("Output:", count_characters(user_input))
