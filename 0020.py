def isValid(s):
    b_nums = {
        "(": 1,
        ")": -1,
        "[": 2,
        "]": -2,
        "{": 3,
        "}": -3
    }
    queue = []
    for char in s:
        if len(queue) == 0:
            queue.append(b_nums[char])
        elif queue[-1] + b_nums[char] == 0 and queue[-1] > b_nums[char]:
            queue.pop()
        else:
            queue.append(b_nums[char])
    return len(queue) == 0

result = isValid("()[]{}")
print("True:", result)

result = isValid("([)]")
print("False:", result)