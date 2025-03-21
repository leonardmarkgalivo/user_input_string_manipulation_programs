# Ask the user to input their full name.
# Reverse the casing of each letter.

def reverse_casing(name):
    # Swaps the case of each letter in the input string
    return name.swapcase()

# Print the reversed-case name.
user_input = input("Enter your full name: ")
print("Output:", reverse_casing(user_input))
