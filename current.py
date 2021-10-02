def isMatch(s: str, p: str) -> bool:
    inf = False
    raw = ''
    cooked = ''
    while p != '':
        if p[-1] == '*':
            if p[-2] == '.':
                return True
            cooked = p[-2:] + cooked
            p = p[:-2]
        else:
            raw = p[-1] + raw
            p = p[:-1]

    #Above part works
    #If you can't get past a part of raw, use cooked. If still doesn't work, repeat
    #Then go through cooked

    for i in range(-1, -len(p) - 1, -1):
        if p[-1] == '*':
            inf = True
            p = p[:-1]
        elif p[-1] == '.':
            if inf:
                return True
            else:
                p, s = p[:-1], s[:-1]
        else:
            if inf:
                inf = False
                for _ in range(-1, -len(s) - 1, -1):
                    if p[-1] == s[-1]:
                        s = s[:-1]
                p = p[:-1]
            elif len(s) > 0 and p[-1] == s[-1]:
                p, s = p[:-1], s[:-1]
            else:
                return False
    return s == ''

s = "aa"
p = "ab*a"

s = "mississippi"
p = "mis*is*p*."
print(isMatch(s, p))