def generateParenthesis(n):
    def perms(input):
        res, enc = [], []
        for s in input:
            for i in range(len(s) + 1):
                for j in range(len(s) + 2):
                    temp = s
                    temp = temp[:i] + "(" + temp[i:]
                    temp = temp[:j] + ")" + temp[j:]
                    if temp not in enc:
                        enc.append(temp)
                        if check(temp) and temp not in res:
                            res.append(temp)
        return res

    def check(s):
        progress = False
        while True:
            for i in range(len(s) - 1):
                if s[i] + s[i + 1] == "()":
                    s = s[:i] + s[i + 2:]
                    progress = True
                    break
            if not progress:
                return False
            elif s == "":
                return True
            else:
                progress = False

    res = ["()"]
    while n > 1:
        res = perms(res)
        n -= 1
    return res