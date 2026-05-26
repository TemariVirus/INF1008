def isValid(c: int, r: int, chessboard: list[list[int]]) -> bool:
    for row in range(r):
        col = chessboard[row].index(1)
        if c == col or abs(c - col) == (r - row):
            return False
    return True


# Dunno how to demo this lol
