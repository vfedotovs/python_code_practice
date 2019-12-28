def twosum_dict(nums, target):
    hash_table = {}
    for i in range(len(nums)):    # hash table
        hash_table[nums[i]] = i
    for i in range(len(nums)):
        if target - nums[i] in hash_table:  # look up in dict for match
            if hash_table[target - nums[i]] != i:
                return [i, hash_table[target - nums[i]]]
    return []


#print(twosum_dict([2, 7, 11, 15, 4, 5, 6, 3], 9))
print(twosum_dict([4, 5, 3, 2, 1, 6, 7], 12))