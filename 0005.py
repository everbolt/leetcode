def longestPalindrome(s: str) -> str:
    def check(s):
        if len(s) % 2 == 0: #Even
            first, second = s[:len(s) // 2], s[len(s) // 2:]
        else:
            first, second = s[:len(s) // 2], s[len(s) // 2 + 1:]
        return first == second[::-1]
    best = s[0]
    for i, c in enumerate(s):
        for p in range(len(s) - 1, i, -1):
            temp = s[i:p + 1]
            if len(temp) < best_len:
                break
            elif c == s[p] and check(temp) and len(best) < len(temp):
                best = temp
                best_len = len(best)
    return best


s = "a"
print(longestPalindrome(s))