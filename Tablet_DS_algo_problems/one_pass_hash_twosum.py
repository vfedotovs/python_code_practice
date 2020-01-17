def twosum_dict(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return([hash_table[target - num], i])
            break    # 
        hash_table[num] = i
    return([])

print(twosum_dict([4, 5, 3, 2, 1, 6, 7], 12))



