def distribute_fairly(debts, total_amount):
    # Sort people by amount owed to handle smaller debts first
    sorted_people = sorted(debts.items(), key=lambda x: x[1])
    n = len(sorted_people)
    
    distribution = {}
    remaining_amount = total_amount
    
    for i, (name, owed) in enumerate(sorted_people):
        # Calculate the "fair share" if we split remaining amount 
        # equally among the remaining people
        num_remaining = n - i
        fair_share = remaining_amount / num_remaining
        
        # They get either their fair share or what they are owed, 
        # whichever is smaller.
        given = min(owed, fair_share)
        
        distribution[name] = given
        remaining_amount -= given
        
    return distribution

# --- Test Cases ---
# example_1 = {'a': 10, 'b': 5}
# amount_1 = 10
# print(f"Result 1: {distribute_fairly(example_1, amount_1)}") 
# # Output: {'b': 5.0, 'a': 5.0}

example_2 = {'a': 20, 'b': 5, 'c': 10}
amount_2 = 18
print(f"Result 2: {distribute_fairly(example_2, amount_2)}")
# Output: {'b': 5.0, 'c': 6.5, 'a': 6.5}