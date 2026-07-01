import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])

# print(arr1.sum())
# print(arr2.sum())
# print(arr2[1].sum())
# print(arr2)
# print(arr2.sum(axis=0))
# print(arr2.sum(axis=1))

# print(np.square(arr1))
# print(np.square(arr1[2]))
# print(np.square(arr2[2][2]))

# arr3= np.array([[1,2,3,4], [4,5,6,7], [7,8,9,10]])
# print(arr3[2][3]+10)
# print(arr3[2][3]-10)
# print(arr3[2][3]*10)
# print(arr3[2][3]//10)

arr3 = np.array([1,2,3,4,5])
arr4 = np.array([10,20,30,40,50])

# arr5 = arr3+arr4
# print(arr5)

# Indexing and Slicing in NumPy
# 1. One Dimensional Array
a1 = np.array([1,2,3,4,5,6,7,8,9])
# print(a1[2])
# print(a1[-1])
# print(a1[1:3])
# print(a1[2:])
# print(a1[:3])

# 2. Two Dimensional Array
a2 = np.array([[1,2,3,4], [5,6,7,8], [3,4,5,6], [7,8,9,0], [1,2,5,4], [5,6,7,8]])

# print(a2)
# print(a2[3])
# print(a2[3,2])
# print(a2[3][2])
# print(a2[-2])
# print(a2[0:2, 2:3])
# print(a2[0:2, 2:])

# 3. Boolean Indexing
# a3 = a2>5
# print(a3)

# Iteration in NumPy
# for i in a1:
    # print(i)

# for i in a2:
#     print(i)
#     for j in i:
#         print(j)

# a5 = np.array([[[1,2,3,43],[5,6,7,7],[9,2,5,7]],[[1,2,3,43],[5,6,7,7],[9,2,5,7]]])
# print(a5)


# Stacking in NumPy

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,21,32,40,50])

vertical = np.vstack([arr1, arr2])
# print(vertical)

horizontal = np.hstack([arr1,arr2])
# print(horizontal)

concat = np.concatenate([arr1,arr2])
# print(concat)