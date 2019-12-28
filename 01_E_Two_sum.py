
"""
Problem
Given list of ints return list of indexes that  in pair adds sum to traget
example 2 + 7 = 9

list = [2,7,11,15]
target = 9
return list of indexes [0,1]
"""


def twosum(nums: list, target: int):

    for i in range(len(nums)):
        left = nums[i + 1:]
        for j in range(len(left)):
            if (nums[i] + left[j]) == target:
                return i, j + i + 1


print(twosum([2, 7, 11, 15, 4, 5, 6, 3], 9))
print(twosum([4, 5, 3, 2, 1, 6, 7], 12))


def twosum_dict(nums, target):
    hash_table = {}
    for i in range(len(nums)):    # hash table
        hash_table[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hash_table:
            if hash_table[target - nums[i]] != i:
                return [i, hash_table[target - nums[i]]]
    return []


print(twosum_dict([2, 7, 11, 15, 4, 5, 6, 3], 9))
print(twosum_dict([4, 5, 3, 2, 1, 6, 7], 12))
