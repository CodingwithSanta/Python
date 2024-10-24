def atm_distribution(amount):
    denominations = [2000, 100, 50, 20, 10, 5, 1]  # Example denominations in descending order
    distribution = {}  # Dictionary to store the distribution
    
    for demon in denominations:
        if amount >= demon:
            distribution[demon] = amount // demon  # Get number of notes for current denomination
            amount = amount % demon  # Update the remaining amount

    return distribution

# Test function
amount = int(input("Enter the amount to withdraw: "))
result = atm_distribution(amount)
print("ATM money distribution:", result)
