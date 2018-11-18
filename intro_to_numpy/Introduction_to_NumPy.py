
# coding: utf-8

# # Introduction to Numpy
# Learning Numpy!

# In[2]:


import numpy as np
np.__version__


# ## Differences between lists and NumPy Arrays
# - An array's size is immutable. You cannot append, insert, or remove elements, like you can with a list.
# - All of an array's elements must be of the same data type. 
# - A NumPy array behaves in a pythonic fashion. You can len(my_array) just like you would assume.

# In[3]:


gpas_as_list = [4.0, 3.286, 3.5]


# In[14]:


# Can have elements appended to it.
gpas_as_list.append(4.0)
# Can have multiple data types
gpas_as_list.insert(1, "whatevs")
gpas_as_list.pop(1)


# In[15]:


gpas_as_list


# In[7]:


gpas = np.array(gpas_as_list)


# In[9]:


get_ipython().run_line_magic('pinfo', 'gpas')


# ## Indexing NumPy Arrays

# ### ---Retrieve Item Size

# In[10]:


gpas.itemsize


# In[11]:


gpas.size


# In[12]:


len(gpas)


# In[13]:


gpas.nbytes


# ### ---Generate practice data with random() function

# In[8]:


rand_array = np.random.RandomState(43)
rand_log = rand_array.randint(30, 180, size=100, dtype=np.uint16)
rand_log


# ## Indexing Boolean Arrays

# In[9]:


rand_log < 60


# ### ---Fancy indexing with a boolean array 
# Using a boolean array index is orders of magnitude faster than using a for loop. 

# In[14]:


rand_log[rand_log < 60]


# ### --- Using boolean expressions to index an array
# 
# Make sure to use ampersand instead of typing out 'and'

# In[15]:


np.array([False, True, True]) & np.array([True, False, True])


# In[19]:


rand_log[(rand_log < 60) & (rand_log > 0)] 


# ## Slicing Practice
# In Python, slices don't return a copy; they return a view of the data
# A <b>view</b> references the same value in memory

# In[20]:


flowers = ["daisy", "rose", "tulip", "daffodil", "orchid", "sunflower"]
flowers[1:3]


# In[22]:


flowers[:-1]


# In[29]:


practice = np.arange(42)
practice.shape = (7,6)
practice


# In[30]:


practice[2,1]


# In[31]:


practice[2:5]


# In[32]:


practice[2:4, 3::2]      #two colons skips over selected columns


# In[33]:


practice.base is None


# In[34]:


practice.flags['OWNDATA']


# ### Using NumPy to do linear algebra

# In[7]:


orders = np.array([
    [2, 0, 0, 0],
    [4, 1, 2, 2], 
    [0, 1, 0, 1],
    [6, 0, 1, 2]
])
totals = np.array([3, 20.50, 10, 14.25])


# In[8]:


prices = np.linalg.solve(orders, totals)
prices

