#Ask the user to input their full name in incorrect casing.
#Convert the input to PascalCase (capitalize first letter of each word, no spaces).
#Print the PascalCase name.

full_name = input("Enter your full name in incorrect casing: ")
print(full_name.title().replace(" ", ""))  # Converts to PascalCase
