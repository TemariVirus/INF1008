import sys

def longest_palindromic_subsequence(s: str) -> int:
    s = s.upper()
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            start = j
            end = start + i + 1
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
    return dp[0][n - 1]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_string_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            input_string = file.read().strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

    result = longest_palindromic_subsequence(input_string)
    #print(f"{result}")
    print(f"Longest Palindromic Subsequence Length: {result}")


if __name__ == "__main__":
    main()

