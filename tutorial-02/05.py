def checkBrackets(counts: dict[str, int], c: str, open: str, end: str):
    counts.setdefault(open, 0)
    if c == open:
        counts[open] += 1
    elif c == end:
        if counts[open] <= 0:
            print("Not legal")
            exit()
        counts[open] -= 1
    else:
        return False
    return True


if __name__ == "__main__":
    counts = dict()
    for c in input():
        _ = (
            # Short-circuit to save time
            checkBrackets(counts, c, "(", ")")
            or checkBrackets(counts, c, "[", "]")
            or checkBrackets(counts, c, "{", "}")
        )

    for v in counts.values():
        if v > 0:
            print("Not legal")
            exit()

    print("Legal")
