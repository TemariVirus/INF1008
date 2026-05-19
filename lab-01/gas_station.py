# Returns index of first element that is larger than val
def binary_search(arr, val):
    head = 0
    tail = len(arr) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if val >= arr[mid]:
            head = mid + 1
        else:
            tail = mid - 1
    return head


# Function to calculate the minimum number of refueling stops
def min_stops(D, M, S):
    d = 0
    stops = 0
    while d + M < D:
        i = binary_search(S, d + M)
        if i == 0:
            return -1  # Impossible
        d = S[i - 1]
        stops += 1
        S = S[i:]

    return stops


if __name__ == "__main__":
    # Input
    D = int(input("Enter the total distance (D): "))
    M = int(input("Enter the maximum fuel range (M): "))
    S = list(
        map(
            int,
            input(
                "Enter the distances of the gas stations separated by spaces: "
            ).split(),
        )
    )

    # Output
    result = min_stops(D, M, S)
    if result != -1:
        print(f"Minimum number of stops: {result}")
    else:
        print("Destination is not reachable.")
