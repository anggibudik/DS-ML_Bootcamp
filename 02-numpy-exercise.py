"""
Exercise for 2nd part of DS-ML bootcamp (NumPy)

Note:
This file uses Jupyter kernel on VS code text editor
"""
# In[1]:
import numpy as np

# %% Create an array of 10 zeros
np.zeros(10)

# %% Create an array of 10 ones
np.ones(10)

# %% Create an array of 10 fives
np.zeros(10) + 5
# or np.ones(10) * 5

# %% Create an array of integers from 10 to 50
np.arange(10,51)

# %% Create an array of all even integers from 10 to 50
np.arange(10,51,2)

# %% Create a 3x3 matrix with values ranging from 0 to 8
np.arange(9).reshape(3,3)

# %% Create a 3x3 identity matrix
np.eye(3)

# %% Generate random number between 0 to 1 with numpy
# np.random.rand() # rand() basically return between 0 to 1
np.random.rand(1) # this will return the result as an array

# %% Generate array of 25 random numbers from standard normal distribution
np.random.randn(25)

# %% Create the instructed matrix (from lecture notebook module)
np.linspace(0.01,1,100).reshape(10,10)
# or
# np.arange(0.01, 1.01, 0.01).reshape(10,10)

# %% Create an array of 20 linearly spaced points between 0 and 1
np.linspace(0,1,20)

# In[2]:
# NUMPY INDEXING AND SELECTION

# Reproduce the results on the notebook exercise module
# based on the given matrix "mat" below:
mat = np.arange(1,26).reshape(5,5)
mat

# %% Reproduce the 1st result
mat[2:,1:]

# %% Reproduce the 2nd result
mat[3,4]

# %% Reproduce the 3rd result
# mat[:3,1].reshape(3,1)
# or
mat[:3,1:2]

# %% Reproduce the 4th result
mat[4]
# or
# mat[-1] # only if you're sure to obtain the last array

# %% Reproduce the 5th result
mat[3:]
# or
# mat[3:5,:]

# In[3]:
# Do the following instruction using "mat" 2D array

# %% Get the sum of all element values in mat
np.sum(mat)
# or
# mat.sum()

# %% Get the standard deviation of mat elements
np.std(mat)
# or
# mat.std()

# %% Get the sum of all columns in mat
np.sum(mat,axis=0)
# or
# mat.sum(axis=0)

# %% (EXTRA FOR MYSELF) sum of all row in mat
mat.sum(axis=1)

# %%
