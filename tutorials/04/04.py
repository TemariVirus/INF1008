from math import ceil, sqrt


# Probably O(n!) time and space.
def recursive(n: int) -> int:
    return 0 if n <= 0 else 1 + min(max(i, recursive(n - i - 1)) for i in range(n))


# O(n) time and space.
# Probably not what they wanted lol.
def recursive2(n: int) -> int:
    def inner(n: int, i: int) -> int:
        return i if n <= i else inner(n - i, i + 1)

    return inner(n, 1)


# O(n^2) time, O(n) space.
def dp(n: int) -> int:
    min_drops = [1]
    for i in range(1, n):
        min_drops.append(1 + min(max(j, min_drops[i - j - 1]) for j in range(i)))
    return min_drops[-1]


# O(1) time and space. Screw dynamic programming.
def direct(n: int) -> int:
    # Strategy to guarantee solution with minimal number of egg drops:
    # We partition the storeys into blocks of decreasing size as the storeys get higher.
    # The first egg is used to linear scan through the blocks to find the block that contains the target storey.
    # The second egg is used to linear scan through the storeys in the block to find the target storey.
    #
    # For example, for a building with storeys 1 to 100:
    # The first egg is dropped at storey 14, then 14 + 13 = 27, then 27 + 12 = 39, etc. until it breaks.
    # Suppose that the first egg broke at storey 27.
    # Then, the second egg is dropped from storey 15, 16, etc. until it breaks and the target storey has been found.
    # There is an edge case where the first egg does not break after being dropped from storey 14 + 13 + ... + 4 = 99,
    # in which case the second egg is dropped from storey 100 and the target storey is found in 12 drops.
    # This strategy requires at most i + (14 - i) = 14 egg drops.
    #
    # This strategy can be generalised to an n-storey building:
    # Let S(x) denote 1 + 2 + ... + (x - 1) + x
    # The first egg is dropped until it breaks from storeys:
    # S(m) - S(m - 1), S(m) - S(m - 2), ... , S(m)
    # where m is the smallest integer such that S(m) >= n.
    # Let S(m) - S(m - i) denote the storey where the first egg broke.
    # The second egg is dropped until it breaks from storeys:
    # S(m) - S(m - i - 1) + 1, S(m) - S(m - i - 1) + 2, ... , S(m) - S(m - i) - 1
    # It can be shown that at most i + (m - i) = m egg drops are required.
    #
    #         S(m) >= n
    #   m(m+1) / 2 >= n
    # m^2 + m - 2n >= 0
    #            m >= (sqrt(1 + 8n) - 1) / 2
    return ceil(sqrt(0.25 + 2 * n) - 0.5)


if __name__ == "__main__":
    # print(f"recursive: {recursive(100)}")
    print(f"recursive: {recursive2(100)}")
    print(f"DP: {dp(100)}")
    print(f"direct: {direct(100)}")
