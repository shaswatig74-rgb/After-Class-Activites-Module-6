Armstrong_number = int(input("Enter a number: "))
number_of_digits = len(str(Armstrong_number))
print("Number of digits:", number_of_digits)

# Calculate sum of cubes of digits
sum_of_powers = 0
for digit in str(Armstrong_number):
    print("Digit:", digit)
    sum_of_powers += int(digit) ** number_of_digits  # generalized for n-digit numbers

# Check Armstrong condition
if sum_of_powers == Armstrong_number:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")

    
