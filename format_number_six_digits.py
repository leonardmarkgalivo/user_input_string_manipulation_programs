# Ask the user to input a number (0-1000).
# Format the number into 6-digit format by adding leading zeros.

def format_number(number):
    # Converts the input number to a 6-digit string with leading zeros
    return str(number).zfill(6)

# Print the formatted number.
user_input = input("Enter a number (0-1000): ")
print("Output:", format_number(user_input))
