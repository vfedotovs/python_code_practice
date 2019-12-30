
"""
Problem find smallest pair sum
[101,1,21,3,5,63,44,21,-1,-3,-5] --> x mand return both indexes

"""
A = [-6, 101, 1, 21, 3, 5, 4, 63, 44, 21, -1, -3, ]
amin = min(A)
s = 0
B = []

for i in range(len(A)):
    for j in range(1, len(A)):
        if A[i] != A[j]:
            s = A[i] + A[j]
            B.append(s)

print(min(B))

d = {}
for key, value in enumerate(A):
    d.update({value: key})

print(d)

index_list = []
min_list = []
min = 9999
for k, v in d.items():
    for a, b in d.items():
        # print(k, "-->",a)
        if k != a:
            curr_min = k + a
            if curr_min < min:
                print("Found new min pair summ >>>", k, "-->", a, curr_min)
                min = curr_min
                min_list.append(min)
                index_list.append(v)
                index_list.append(b)


print("Min pair sum : ", min_list[-1])
print("Both element indexes", index_list[-2:])
