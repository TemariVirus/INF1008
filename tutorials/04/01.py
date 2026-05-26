def gcd(n: int, m: int) -> int:
    # Sometimes short code is the hardest to read lol
    return gcd(m, n) if n < m else m if n % m == 0 else gcd(m, n % m)

def example(n: int, m: int) -> None:
    print(f"gcd({n}, {m}) = {gcd(n, m)}")

if __name__ == "__main__":
    example(1, 2)
    example(100, 23)
    example(100, 24)
    example(24, 100)
