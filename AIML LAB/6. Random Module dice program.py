import random

def roll_dice(num_dice=1):
    """Simulate rolling `num_dice` dice and return the results."""
    results = []
    
    # Roll the dice `num_dice` times
    for _ in range(num_dice):
        result = random.randint(1, 6)  # Generate a random number between 1 and 64

        results.append(result)
    
    # Print each roll result and the total
    print(f"Rolling {num_dice} dice...")
    print("Results:", results)
    print("Total:", sum(results))
    
    return results

# Main program to roll dice
if __name__ == "__main__":
    # Roll a single die by default or multiple if specified
    number_of_dice = int(input("Enter the number of dice to roll: "))
    roll_dice(number_of_dice)