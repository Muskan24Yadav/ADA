class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(W, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # Total value in knapsack
    for item in items:
        if W == 0:
            break

        if item.weight <= W:
            # Take the whole item
            W -= item.weight
            total_value += item.value
        else:
            # Take fraction of the item
            fraction = W / item.weight
            total_value += item.value * fraction
            W = 0  # Knapsack is full

    return total_value

# Sample input
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]

capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in knapsack: {max_value:.2f}")
