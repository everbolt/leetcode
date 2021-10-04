def threeSumClosest(nums, target) -> int:
    nums.sort()
    best = sum(nums[:3])
    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if target == current_sum:
                return target
            
            if abs(current_sum - target) < abs(best - target):
                best = current_sum

            if current_sum < target:
                j += 1
            elif current_sum > target:
                k -= 1
    return best


nums = [1,1,-1,-1,3]
target = -1
print(threeSumClosest(nums, target))