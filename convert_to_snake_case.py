#Ask the user to input their full name in incorrect casing.
#Convert the input to lowercase.
#Replace spaces with underscores (_).
#Print the snake_case formatted name.

full_name = input("Enter your full name in incorrect casing: ")
print(full_name.lower().replace(" ", "_"))  # Converts to snake_case
