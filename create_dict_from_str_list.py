    
def create_hash_table(A):
    hash_table = {}
    for i, num in enumerate(A):
        hash_table[num] = i
    return hash_table

list = ['h','e','l','l','o',' ','w','o','r','l','d']
num_list = [22,33,445,666,123,456,789,11]

print(create_hash_table(list))
print(create_hash_table(num_list))