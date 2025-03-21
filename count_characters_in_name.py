#Ask the user to input their full name.
#Count the number of characters (excluding spaces).
#Print the character count.

full_name = input("Enter your full name: ")
print(len(full_name.replace(" ", "")))  # Counts characters, ignoring spaces
