class Item:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def fractional_knapsack(W, items, n):
    # Sort items by ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0

    # TODO iterate through n and calculate total value
    for item in items[:n]:
        take = min(W, item.weight)
        W -= take
        total_value += item.ratio * take

    return total_value


def main():
    # Input number of items and capacity
    n, W = map(int, input("Enter number of items and knapsack capacity, separated by space: ").split())

    # Input weights
    weights = list(map(int, input("Enter the weights for each item (separated by spaces): ").split()))

    # Input values
    values = list(map(int, input("Enter the values for each item (separated by spaces): ").split()))

    # Construct list of Item objects
    items = [Item(weight=weights[i], value=values[i]) for i in range(n)]

    # Solve the knapsack problem
    max_value = fractional_knapsack(W, items, n)

    print(f"Maximum value that can be carried: {max_value:.2f}")


if __name__ == "__main__":
    main()