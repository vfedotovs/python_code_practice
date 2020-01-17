def twosum(nums: list, target: int):

    for i in range(len(nums)):
        left = nums[i + 1:]
        for j in range(len(left)):
            if (nums[i] + left[j]) == target:
                return i, j + i + 1


#print(twosum([2, 7, 11, 15, 4, 5, 6, 3], 9))
print(twosum([4, 5, 3, 2, 1, 6, 7], 12))
