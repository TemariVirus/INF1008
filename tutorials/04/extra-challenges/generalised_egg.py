# Do NOT modify me
class Eggs:
    def __init__(self, count: int, limit: int, storeys: int) -> None:
        self.count = count
        self.storey_limit = limit
        self.storeys = storeys
        self.drops = 0

    def remaining(self) -> int:
        return self.count

    def drop(self, storey: int) -> bool:
        """Drops an egg from the storey. Returns whether the egg broke."""
        assert self.count > 0, "You ran out of eggs!"
        assert storey > 0, (
            "Storey is underground! (did you use 0-based indexing instead of 1-based indexing?)"
        )
        assert storey <= self.storeys, "Storey is too high!"
        self.drops += 1
        if storey > self.storey_limit:
            self.count -= 1
            return True
        return False


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
# Write an algorithm that return the correct storey in the least number of egg drops.
# If the eggs break from the first storey, return 0.
# If the eggs do not break from any storey, return the top storey.
#
# Inputs:
#   storeys - The number of storeys in the building.
#   eggs    - The number of eggs to drop. You may only call remaining() and drop().
#
# Constraints:
#   1 <=   storeys  <= 10_000
#   1 <= eggs.count <= 100
def egg_drop(storeys: int, eggs: Eggs) -> int:
    # Time complexity:  O(eggs * storeys^2)
    # Space complexity: O(eggs * storeys)
    from math import inf

    # We do the same thing as egg_drop_count(), but this time we also keep track of which
    # storey drops led us to the minimum number of egg drops.
    min_storeys = (
        [[0 for _ in range(storeys + 1)]]  # Nothing to do with 0 eggs
        + [
            [0] for _ in range(eggs.remaining())
        ]  # Nothing to do when there are 0 storeys
    )
    # Keep track of the minimum number of drops needed for each storey with each number of eggs.
    # min_drops[eggs][storeys] is the solution for egg_drop_count(storeys, eggs)
    min_drops = (
        [[inf for _ in range(storeys + 1)]]  # There is no solution with 0 eggs
        + [
            [0] for _ in range(eggs.remaining())
        ]  # 0 egg drops are needed when there are 0 storeys
    )
    # Bottom-up DP.
    # Find the solution for each number of storeys
    for top_storey in range(1, storeys + 1):
        # Find the solution for each number of eggs
        for eggs_left in range(1, eggs.remaining() + 1):
            min_drop_storey = 1
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
                if drops_needed < min_drops_needed:
                    min_drop_storey = n
                    min_drops_needed = drops_needed
            min_storeys[eggs_left].append(min_drop_storey)
            min_drops[eggs_left].append(min_drops_needed)

    # Drop the eggs according to min_storeys which represents the optimal strategy
    lower = 1
    upper = storeys
    while lower <= upper:
        height = upper - lower + 1
        drop_storey = lower + min_storeys[eggs.remaining()][height] - 1
        if eggs.drop(drop_storey):
            upper = drop_storey - 1
        else:
            lower = drop_storey + 1
    # lower is now the lowest storey where the egg breaks
    return lower - 1


# Example usage of Eggs API
def egg_drop_linear(storeys: int, eggs: Eggs) -> int:
    for i in range(1, storeys + 1):
        if eggs.drop(i):
            # Egg broke
            return i - 1
    # Egg didn't break
    return storeys


def test(storeys: int, eggs: int, answer: int, max_drops: int) -> None:
    e = Eggs(eggs, answer, storeys)
    assert egg_drop(storeys, e) == answer
    assert e.drops <= max_drops


# Run `python generalised_egg.py` (or run this file) to run the tests.
if __name__ == "__main__":
    test(1, 1, 0, 1)
    test(1, 1, 1, 1)
    test(100, 1, 69, 100)
    test(6, 2, 6, 3)
    test(7, 2, 4, 4)
    test(100, 2, 14, 14)
    test(105, 2, 23, 14)
    test(106, 2, 41, 15)
    test(100, 3, 89, 9)
    test(300, 3, 231, 13)
    test(377, 3, 107, 13)
    test(378, 3, 6, 14)
    test(7, 4, 6, 3)
    test(8, 4, 3, 4)
    test(14, 3, 7, 4)
    test(15, 3, 15, 5)
    test(15, 10, 15, 4)
    test(16, 10, 0, 5)
    test(67, 67, 14, 7)
    test(64, 67, 54, 7)
    test(63, 67, 1, 6)
    test(1, 100, 1, 1)
    test(10, 100, 5, 4)
    test(500, 100, 123, 9)
    test(500, 1, 500, 500)
    test(500, 2, 0, 32)
    test(500, 3, 321, 15)
    test(500, 42, 431, 9)
