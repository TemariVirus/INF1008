def same_birthday_prob(n: int) -> float:
    # Find the probability that no one shares a birthday
    acc = 1
    for i in range(1, n):
        # Assume there are 365 days in a year
        acc *= (365 - i) / 365
    # Take the complement
    return 1 - acc


if __name__ == "__main__":
    i = 2
    while same_birthday_prob(i) < 0.5:
        i += 1
    print(i)  # 23
