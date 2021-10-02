def twoSum(nums: List[int], target: int) -> List[int]:
    idx = dict(zip(nums, nums))
    for i in range(len(nums)):
        comp = target - nums[i]
        try:
            if idx[comp] != None:
                x = nums.index(comp)
                if x != i: return [i, x]
        except:
            pass
# Key to this working is that dict overwrites prior defined keys
# if the same key is re-initialized. This means that the index of 
# the last instance of an int will be stored in the dict
# allowing you to directly check if there is a duplicate or not
# using nums.index(comp)
