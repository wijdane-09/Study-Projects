# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop: iterate over each row using while loop
while row < size:
    # Inner loop: print asterisks for each column in the current row
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to next line after each row
    row += 1  # Increment row counter
