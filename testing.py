def findPairsSummingToK(a, m, k):
    count = 0
    r = range(m)
    for i in range(len(a) - m + 1):
        current = a[i: i + m]
        track = dict(zip(current, r))
        for j, v in enumerate(current):
            try:
                if j != track[k - v]:
                    count += 1
                    break
            except:
                pass
    return count

a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10
print(findPairsSummingToK(a, m, k))