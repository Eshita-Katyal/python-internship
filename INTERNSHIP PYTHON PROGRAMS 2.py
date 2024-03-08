#!/usr/bin/env python
# coding: utf-8

# Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# Original Tuple:
# (4, 3, 2, 2, -1, 18)
# Product - multiplying all the numbers of the said tuple: -864
# Original Tuple:
# (2, 4, 8, 8, 3, 2, 9)
# Product - multiplying all the numbers of the said tuple: 27648

# In[2]:


ORIGINAL_TUPLE1 = [4,3,2,2,-1,18]
ORIGINAL_TUPLE2 = [2,4,8,8,3,2,9]
def prod(val) : 
    res = 1
    for ele in val: 
        res *= ele 
    return res  
res = prod(list(ORIGINAL_TUPLE1))
def prod(val) : 
    res1 = 1
    for ele in val: 
        res1 *= ele 
    return res1
res1 = prod(list(ORIGINAL_TUPLE2))
print("The product of tuple elements are : "+str(res)
)
print("The product of tuple elements are : "+str(res1)
)


# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]

# In[3]:


def average_tuple(nums):
    result = [sum(x)/len(x) for x in zip(*nums)]
    return result
nums = ([10,10,10,12],[30,45,56,45],[81,80,39,32],[1,2,3,4])
print("Original Tuple: ")
print(nums)
print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums))
nums1 =([1,1,-5],[30,-15,56],[81,-60,-39],[-10,2,3])
print("\nOriginal Tuple: ")
print(nums1)
print("\nAverage value of the numbers of the said tuple of tuples:\n", average_tuple(nums1))

