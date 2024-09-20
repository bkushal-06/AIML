def multiplication_table(number):
    """Print the multiplication table of the given number up to 20."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 21):  # Loop from 1 to 20
        result = number * i
        print(f"{number} x {i} = {result}")

# Main program
if __name__ == "__main__":
    # Get user input
    user_number = int(input("Enter a number to get its multiplication table up to 20: "))
    multiplication_table(user_number)
    