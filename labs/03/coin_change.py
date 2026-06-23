import sys
import math

def coin_change(coins, amount):
    dp = [0]
    for target in range(1, amount + 1):
        val = math.inf
        for c in coins:
            left = target - c
            if left < 0:
                continue
            val = min(val, dp[left] + 1)
        dp.append(val)
    return -1 if math.isinf(dp[amount]) else dp[amount]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("File is empty.", file=sys.stderr)
                sys.exit(1)

            amount = int(lines[0].strip())

            if len(lines) < 2:
                print("No coin values provided.", file=sys.stderr)
                sys.exit(1)

            coin_values = list(map(int, lines[1].strip().split()))
    except FileNotFoundError:
        print(f"Error opening file: {filename}", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("File content is not in the expected format.", file=sys.stderr)
        sys.exit(1)

    result = coin_change(coin_values, amount)
    print(result)

if __name__ == "__main__":
    main()
