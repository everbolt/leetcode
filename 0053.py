def maxSubArray(nums):
    max_sum = -1 * float('inf')
    current_sum = 0
    for i, iv in enumerate(nums):
        current_sum += iv
        if current_sum > max_sum:
            max_sum = current_sum
        current_sum = max(0, current_sum)
    return max_sum