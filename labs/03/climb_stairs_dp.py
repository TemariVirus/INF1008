import sys

def climb_stairs_dp(n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def check_recursion(filename: str, function_name: str) -> bool:
    count = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                if function_name in line:
                    count += 1
    except FileNotFoundError:
        print(f"Warning: Could not find the file '{filename}' to check recursion.", file=sys.stderr)
        return False  # Assume not recursive if file isn't there
    return count < 1

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>", file=sys.stderr)
        sys.exit(1)

    if check_recursion("climb_stairs_dp.py", "climb_stairs_dp"):
        print("Error: Function is recursive, please code a solution using bottom-up dynamic programming (tabulation) instead.", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter a number.", file=sys.stderr)
        sys.exit(1)

    result = climb_stairs_dp(n)
    print(f"{result}")

if __name__ == "__main__":
    main()
