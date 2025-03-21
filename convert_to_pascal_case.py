# Ask the user to input their full name in incorrect casing.
# Convert the input to PascalCase (capitalize first letter of each word and remove spaces).

def to_pascal_case(name):
    # Converts the input string to PascalCase
    return name.title().replace(" ", "")