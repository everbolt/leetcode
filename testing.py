x = [2,7,11,15, 4, 20, 3]
target = 9

def twoSum(x, target):
    for first in range(len(x)):
        for second in range(first + 1, len(x)):
            if x[first] + x[second] == target:
                return [first, second]

print(twoSum(x, target))