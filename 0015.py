#Note, this barely passes the runtime maxmimum
def threeSum(nums):
    nums.sort()
    dnums, box = {}, []
    for i in nums:
        try: dnums[i] += 1
        except: dnums[i] = 1
    keys = dnums.keys()

    while len(nums) >= 3 and nums[0] <= 0:
        i = nums[0]
        if nums[-1] + nums[-2] >= i:
            for j in nums[1:]:
                k = -1 * (i + j)
                if k in keys:
                    if k == i and k == j and dnums[k] < 3:
                        break
                    elif (k == i or k == j) and dnums[k] < 2:
                        break
                    lst = sorted([i, j, k])
                    if lst not in box:
                        box.append(lst)
        nums.pop(0)
    return box

entry = [12,0,3,-14,5,-11,11,-5,-2,-1,6,-7,-10,1,4,1,1,9,-3,6,-15,0,6,1,6,-12,3,7,11,-6,-8,0,9,3,-7,-1,7,-10,1,13,-4,-7,-9,-7,9,3,1,-13,-3,13,8,-11,-9,-8,-3,4,-13,7,-11,5,-14,-4,-9,10,6,-9,-6,-9,-12,11,-11,-9,11,-5,0,-3,13,-14,-1,-13,7,-7,14,5,0,-4,-6,-6,-11,-2,14,-10,2,12,8,-7,-11,-13,-9,14,5,-5,-9,1,-2,6,5,-12,-1,-10,-9,-9,-10,12,11]

test = [0, 0, 0]

print(threeSum(entry))