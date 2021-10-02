def myAtoi(s: str) -> int:
    #Parse until +- or digit
    #Parse digits until non-digit
    #Check bounds
    neg, result = 1, 0
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    if len(s) > 0 and s[0] == '-':
        neg, s = -1, s[1:]
    elif len(s) > 0 and s[0] == '+':
        s = s[1:]
    while len(s) > 0 and s[0].isdigit():
        result, s = result * 10 + int(s[0]), s[1:]
    return min(max(result * neg, -2**31), 2**31 - 1)
s = "-91283472332"
s = "4193 with words"
#s = "   -42"
print(myAtoi(s))