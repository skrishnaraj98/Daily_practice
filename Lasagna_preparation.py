#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'lasagna_prep.py', '\n# This is a very basic python code to write a logic to understand how much time it takes \n# to make a lasagna dish within certain explicit conditions. \n\nEXPECTED_BAKE_TIME=60      #in minutes\nEXPECTED_PREP_TIME=2       #in minutes for a single layer of lasagna\n\ndef bake_time(spent_time):\n    """\n    :param spent_time: int - baking time elapsed. \n    :return: int - total baking time elapsed. \n    \n    This function takes in an int argument (in minutes) which represents the baking time elapsed. \n    And returns the baking time in minutes. \n    \n    """\n    return spent_time\n\ndef remaining_time(spent_time):\n    """\n    This function doesn\'t have any parameters and returns the remaining time from EXPECTED_BAKE_TIME.\n    \n    """\n    return EXPECTED_BAKE_TIME - spent_time\n\ndef prepartion_time(layers): \n    """\n    :param layers: int - represents the number of layer that we wish to add within the dish. \n    :return: int - represents the total time (in minutes) in preparing the layers of the dish. \n    \n    This function takes in layers as the arguments representing the number of layers and then returns\n    the time in minutes it takes to prepare all of the layers for the lasagna dish. \n    \n    """\n    return layers*EXPECTED_PREP_TIME\n\ndef total_time_elapsed(layers, spent_time):\n    """\n    This function doesn\'t take any arguments and returns the total time (prep+bake) elapsed in \n    cooking the lasagna dish. \n    \n    """\n    return (prepartion_time(layers) + bake_time(spent_time))\n')


# In[14]:


import lasagna_prep

print("Baking time elapsed:",lasagna_prep.bake_time(20),"minutes")
print("Remaining time in Baking:",lasagna_prep.remaining_time(20),"minutes")
print("Lasagna layers prep time:",lasagna_prep.prepartion_time(8),"minutes")
print("Total time Layers prep + bake:",lasagna_prep.total_time_elapsed(8,20),"minutes")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




