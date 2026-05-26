def isPalindrome(s: str) -> bool:
    s = "".join(list(filter(lambda c: c.isalpha(), s))).upper()
    return len(s) == 0 or (s[0] == s[-1] and isPalindrome(s[1:-1]))


def example(s: str) -> None:
    print(f'"{s}" is{"" if isPalindrome(s) else " not"} a palindrome')


if __name__ == "__main__":
    example("palindrome")
    example("Aibohphobia")
    example("Adam, I’m Madam")
    example("Madam, I’m Adam")
