x = 1
y = 1
z = 1
n = 2

# newlist = [expression for item in iterable if condition == True]
# res = [[x, 0, 0] for item in range(x) if x + y + z != n]

res = [[i, j, k] for i in range(x + 1) for j in range(y + 1)
       for k in range(z + 1) if i + j + k != n]

print(res)

# for i in range(z+1):
#     for j in range(y+1):
#         for k in range(x+1):
#             if i + j + k != n:
#                 print([i, j, k])
# print(res, 'res')
