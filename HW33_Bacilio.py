
# coding: utf-8

# In[6]:


# Import CSV file
import pandas as pd
import numpy as np
df = pd.read_csv('Consumer_Complaints.csv')


# In[7]:


rows1 = df.shape
row1 = rows1[0]
df = df[pd.notnull(df['Consumer complaint narrative'])] # ONLY KEEPSROWS WITH NON-NAN VALUES IN COLUMN i
rows2 = df.shape
row2 = rows2[0]
difference = row1 - row2
print("original set had "+str(row1)+" observations")
print(str(difference)+" rows had blank narratives")
print(str(row2)+" observations will be analyzed")


# In[4]:


# histogram for companies directly from the file
from collections import Counter, OrderedDict # CALLS COUNTER FUNCTION
from matplotlib import pyplot # IMPORTS GRAPH FUNCTION
string_counts = Counter(df['Company']) # CREATES A LIST THAT COUNTS THE REPETITIONS OF A STRING
string_counts = OrderedDict(string_counts.most_common())
pyplot.figure(1, figsize=(20, 9)) # CREATES A FIGURE WITH THE DIMENSIONS INDICATED
pd.Series(Counter(string_counts)).plot(kind='bar') # CREATES A SERIE FROM THE LIST
pyplot.suptitle('Company') # GIVES THE MAIN TITLE
pyplot.show() # DISPLAYS THE FIGURE


# In[ ]:


string_counts = Counter(df['Company']) # CREATES A LIST THAT COUNTS THE REPETITIONS OF A STRING
print(str(len(string_counts))+ " companies are listed in the complains")


# In[ ]:


# DATA EXPLORATION FOR RELEVANT CATEGORIES
from collections import Counter, OrderedDict # CALLS COUNTER FUNCTION
from matplotlib import pyplot
categories = ['Product','Sub-product','Issue','Sub-issue']
k = 1
for i in categories:
    string_counts = Counter(df['{0}'.format(i)]) # CREATES A LIST THAT COUNTS THE REPETITIONS OF A STRING
    string_counts = OrderedDict(string_counts.most_common())
    pyplot.figure(k, figsize=(17, 7)) # CREATES A FIGURE WITH THE DIMENSIONS INDICATED
    converted_series=pd.Series(Counter(string_counts)) # CREATES A SERIE FROM THE COUNTER CLASS
    converted_series.plot(kind='bar') # PLOTS THE SERIES INTO BOX PLOT
    pyplot.suptitle('Histogram for "{0}", '.format(i)+str(len(string_counts))+" categories found.") # GIVES THE MAIN TITLE
    pyplot.show() # DISPLAYS THE FIGURE
    k += 1


# In[ ]:


import nltk
import re
import pprint
sent = nltk.corpus.treebank.tagged_sents()[22]
print(nltk.ne_chunk(sent, binary=True))

