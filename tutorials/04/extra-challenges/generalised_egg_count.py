# You are given some eggs, and access to a storeyed building.
# All eggs are identical.
# The aim is to find out the highest storey from which an egg will not break when
# dropped out of a window from that storey.
# If an egg is dropped and does not break, it is undamaged and can be dropped again.
# However, once an egg is broken, it may not be dropped again.
# A dropped egg either breaks completely or is not broken.
# If an egg breaks when dropped from storey n, then it will also break from any
# storey above that.
# If an egg survives a fall from storey n, then it will also survive any fall lower
# than that.
#
# Write an algorithm that returns the minimum number of egg drops required to
# guarantee the correct storey is found.
#
# Inputs:
#   storeys - The number of storeys in the building.
#   eggs    - The number of eggs you start with.
#
# Constraints:
#   1 <= storeys <= 500
#   1 <=   eggs  <= 100
def egg_drop_count(storeys: int, eggs: int) -> int:
    # Time complexity:  O(eggs * storeys^2)
    # Space complexity: O(eggs * storeys)
    from math import inf

    # Keep track of the minimum number of drops needed for each storey with each number of eggs.
    # min_drops[eggs][storeys] is the solution for egg_drop_count(storeys, eggs)
    min_drops = (
        [[inf for _ in range(storeys + 1)]]  # There is no solution with 0 eggs
        + [[0] for _ in range(eggs)]  # 0 egg drops are needed when there are 0 storeys
    )
    # Bottom-up DP.
    # Find the solution for each number of storeys
    for top_storey in range(1, storeys + 1):
        # Find the solution for each number of eggs
        for eggs_left in range(1, eggs + 1):
            # Solution cannot be worse than if we only had 1 egg
            min_drops_needed = top_storey
            # Try dropping the egg at storey n
            for n in range(1, top_storey + 1):
                # If the egg breaks, we know the solution is in the range [1, n - 1].
                # This is the same as egg_drop_count(len([1, n - 1]), eggs_left - 1).
                drops_if_broken = min_drops[eggs_left - 1][n - 1]
                # If the egg does not break, we know the solution is in the range [n + 1, top_storey].
                # This is the same as egg_drop_count(len([n + 1, top_storey]), eggs_left).
                drops_if_not_broken = min_drops[eggs_left][top_storey - n]
                # Add 1 to include this drop
                drops_needed = 1 + max(drops_if_broken, drops_if_not_broken)
                min_drops_needed = min(min_drops_needed, drops_needed)
            min_drops[eggs_left].append(min_drops_needed)

    return int(min_drops[eggs][storeys])


# From Broadman (https://arxiv.org/pdf/2511.18330v2 p3),
# we know that with k eggs and n drops, we can solve at most
# \sum_{j=1}^{k} (n choose j) floors.
# This is clearly a monotonic function in n, so we can invert it with binary search.
def egg_drop_count_fast(storeys: int, eggs: int) -> int:
    # Time complexity:  O(eggs * log(storeys))
    # Space complexity: O(1)

    # Calculates \sum_{j=1}^{k} (n choose j)
    def most_storeys(eggs: int, drops: int) -> int:
        nCj = 1
        acc = 0
        for i in range(eggs):
            nCj *= drops - i
            nCj //= i + 1
            acc += nCj
        return acc

    # Binary search
    lower = 0
    upper = storeys
    while lower < upper:
        mid = (lower + upper) // 2
        current = most_storeys(eggs, mid)
        if current >= storeys:
            upper = mid
        else:
            lower = mid + 1
    return upper


# Run `python generalised_egg_count.py` (or run this file) to run the tests.
if __name__ == "__main__":
    assert egg_drop_count(1, 1) == 1
    assert egg_drop_count(100, 1) == 100
    assert egg_drop_count(6, 2) == 3
    assert egg_drop_count(7, 2) == 4
    assert egg_drop_count(100, 2) == 14
    assert egg_drop_count(105, 2) == 14
    assert egg_drop_count(106, 2) == 15
    assert egg_drop_count(100, 3) == 9
    assert egg_drop_count(300, 3) == 13
    assert egg_drop_count(377, 3) == 13
    assert egg_drop_count(378, 3) == 14
    assert egg_drop_count(7, 4) == 3
    assert egg_drop_count(8, 4) == 4
    assert egg_drop_count(14, 3) == 4
    assert egg_drop_count(15, 3) == 5
    assert egg_drop_count(15, 10) == 4
    assert egg_drop_count(16, 10) == 5
    assert egg_drop_count(67, 67) == 7
    assert egg_drop_count(64, 67) == 7
    assert egg_drop_count(63, 67) == 6
    assert egg_drop_count(1, 100) == 1
    assert egg_drop_count(10, 100) == 4
    assert egg_drop_count(500, 100) == 9
    assert egg_drop_count(500, 1) == 500
    assert egg_drop_count(500, 2) == 32
    assert egg_drop_count(500, 3) == 15
    assert egg_drop_count(500, 42) == 9
