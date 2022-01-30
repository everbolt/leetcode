def fourSum(nums, target):
    if len(nums) < 4:
        return []
    pairs = {}
    res = []
    for i, iv in enumerate(nums):
        for j, jv in enumerate(nums[i + 1:], start = i + 1):
            if i != j:
                total = iv + jv

                pair = (j, i)

                if total not in pairs:
                    pairs[total] = [pair]
                else:
                    pairs[total].append(pair)

    for i, iv in enumerate(nums):
        for j, jv in enumerate(nums[i + 1:], start = i + 1):
            if i != j:
                t = target - iv - jv
                if t in pairs:
                    for pair in pairs[t]:
                        if i not in pair and j not in pair:
                            temp = [iv, jv, nums[pair[0]], nums[pair[1]]]
                            temp.sort()
                            if temp not in res:
                                res.append(temp)
    return res