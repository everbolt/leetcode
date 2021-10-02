def isMatch(s, p):
    def check(s, p):
        if len(s) == len(p) == 0: #Done
            return True
        elif len(s) > 0 and len(p) == 0: #No code left
            return False
        elif len(s) > 0 and (s[-1] == p[-1] or p[-1] == '.'): #Content match
            return check(s[:-1], p[:-1])
        elif p[-2:] == '.*':
            if len(s) == 0:
                return check(s, p[:-2])
            else:
                result = check(s, p[:-2])
                while len(s) > 0:
                    result, s = result or check(s[:-1], p[:-2]), s[:-1]
                return result
        elif p[-1] == '*':
            if len(s) == 0 or s[-1] != p[-2]:
                return check(s, p[:-2])
            else:
                result = check(s, p[:-2])
                while len(s) > 0 and s[-1] == p[-2]:
                    result, s = result or check(s[:-1], p[:-2]), s[:-1]
                return result
        return False
    return check(s, p)

s = "aasdfasdfasdfasdfas"
p = "aasdf.*asdf.*asdf.*asdf.*s"

print(isMatch(s, p))