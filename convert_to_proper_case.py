# Ask the user to input their full name.
# Convert the input to proper case (first letter of each word capitalized).

def to_proper_case(name):
    # Converts the input string to proper case
    return name.title()

# Print the properly formatted name.
user_input = input("Enter your full name: ")
print("Output:", to_proper_case(user_input))
