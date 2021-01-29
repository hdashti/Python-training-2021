# dct = {"a": 100, "b": 400, "c": 600}
# for k,v in dct.items():
#     print(k,"-----",v)

# How index a list - keep a count of iterations
lst = [10, 20, 54, 2, 65, 100]
# Method 1
# for indx in range(len(lst)):
#     print(indx, lst[indx])

#Method 2
for i, val in enumerate(lst):
    print(i, val)