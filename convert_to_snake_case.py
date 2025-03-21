# Ask the user to input their full name in incorrect casing.
# Convert the input to snake_case (lowercase and replace spaces with underscores).

def to_snake_case(name):
    # Converts the input string to snake_case
    return name.lower().replace(" ", "_")