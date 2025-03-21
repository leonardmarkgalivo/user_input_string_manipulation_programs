# Ask the user to input their full name with leading spaces.
# Remove the spaces at the beginning.

def remove_leading_spaces(name):
    # Removes leading spaces from the input string
    return name.lstrip()

# Print the cleaned name.
user_input = input("Enter your full name with leading spaces: ")
print("Output:", remove_leading_spaces(user_input))
