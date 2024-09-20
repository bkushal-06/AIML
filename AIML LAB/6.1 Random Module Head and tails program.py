import random

def coin_toss():
    """Simulate a coin toss and return the result as 'Heads' or 'Tails'."""
    result = random.choice(['Heads', 'Tails'])  # Randomly choose 'Heads' or 'Tails'
    print(f"The coin toss result is: {result}")
    return result

# Main program to toss the coin
print("Tossing the coin...")
coin_toss()
