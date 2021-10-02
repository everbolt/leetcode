def findMedianSortedArrays(nums1, nums2) -> float:
    total_len = len(nums1) + len(nums2)
    merge = [0] * total_len
    for i in range(total_len):
        if nums1 == []:
            merge[i:] = nums2
            break
        elif nums2 == []:
            merge[i:] = nums1
            break
        elif nums1[0] < nums2[0]:
            merge[i]  = nums1[0]
            nums1 = nums1[1:]
        else:
            merge[i] = nums2[0]
            nums2 = nums2[1:]
    if total_len % 2 == 0:
        return (merge[total_len // 2 - 1] + merge[total_len // 2]) / 2
    else:
        return merge[total_len // 2]
    

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))