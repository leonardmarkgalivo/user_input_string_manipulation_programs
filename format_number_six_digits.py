#Ask the user to input a number (0-1000).
#Convert the number into a string.
#Pad it with leading zeros to make it 6 digits long.
#Print the formatted number.

number = input("Enter a number (0-1000): ")
print(number.zfill(6))  # Pads with leading zeros

