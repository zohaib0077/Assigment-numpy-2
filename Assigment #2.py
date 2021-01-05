#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::
# 

# # Question:1
# Convert a 1D array to a 2D array with 2 rows?
# Desired output::
# array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])

# In[3]:


import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_2d = np.reshape(arr, (2, 5))
arr_2d


# # Question:2
# How to stack two arrays vertically?
# Desired Output::
# array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])

# In[15]:


A = np.array([[0,1,2,3,4], [5, 6,7,8,9]])
B = np.array([[1,1,1,1,1], [1,1,1,1,1]])
np.vstack((A,B))


# # Question:3
# How to stack two arrays horizontally?
# Desired Output::¶

# In[16]:


A = np.array([[0,1,2,3,4], [5, 6,7,8,9]])
B = np.array([[1,1,1,1,1], [1,1,1,1,1]])
np.hstack((A,B))


# # Question:4
# How to convert an array of arrays into a flat 1d array?
# Desired Output::
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 
# 

# In[22]:


array1 = np.array([[0,1,2,], [4,5,6 ], [7,8,9]])
array1.flatten() 
array1.reshape([1, 9]) 
  


# # Question:5
# How to Convert higher dimension into one dimension?
# Desired Output::
# array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

# In[33]:


arryy = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
arryy.reshape(-1)


# # Question:6
# Convert one dimension to higher dimension?
# Desired Output::
# array([[ 0, 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 9, 10, 11], [12, 13, 14]])
# 

# In[35]:


a = np.array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
a.reshape(3,5)


# # Question:7
# Create 5x5 an array and find the square of an array?

# In[43]:


b = np.arange(25).reshape((5,5))
np.square(b)


# # Question:8
# Create 5x6 an array and find the mean?

# In[44]:


b = np.arange(30).reshape((5,6))
np.mean(b)


# # Question:9
# Find the standard deviation of the previous array in Q8?

# In[45]:


np.std(b)


# # Question:10
# Find the median of the previous array in Q8?

# In[46]:


np.median(b)


# # Question:11
# Find the transpose of the previous array in Q8

# In[49]:


b.transpose()


# # Question:12
# Create a 4x4 an array and find the sum of diagonal elements

# In[53]:


a = np.arange(16).reshape((4,4))
b = np.diagonal((a) )
sum(b)


# # Question:13
# Find the determinant of the previous array in Q12?

# In[55]:


np.linalg.det(a)


# # Question:14
# Find the 5th and 95th percentile of an array?

# In[65]:


a = np.arange(20)
c = np.percentile(a,5)
d = np.percentile(a,95)
print( c,"\n" ,d)


# # Question:15
# How to find if a given array has any null values?

# In[66]:


np.isnan(a)


# In[ ]:




