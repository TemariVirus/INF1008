import sys

def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number>", file=sys.stderr)
        sys.exit(1)

    number = sys.argv[1]
    try:
        n = int(number)
    except ValueError:
        print("Invalid input. Please provide an integer.", file=sys.stderr)
        sys.exit(1)

    result = climb_stairs(n)
    print(f"{result}")

if __name__ == "__main__":
    main()
