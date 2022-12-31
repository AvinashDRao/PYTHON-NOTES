#!/usr/bin/env python
# coding: utf-8

# # Data types:
# 1.Strings
# 2.List and Tuples
# 3.Dictionary
# 4.Sets
# 
# 1.STRINGS: It is enclosed with codes
#             ex;"hello, world"
#     OPERATORS:
#             + concatination
#             * repetative
#             [] slicing
#             [:] slice ranging
#             in
#             not in
#     STRING METHODS:
#             1.len() =lenght of the string
#             2.capitalize()
#             3.upper()
#             4.lower()
#             5.center()
#             6.count()
#             7.find()
#             8.index()'''

# In[2]:



for letter in "banana":
    print(letter)


# In[3]:


len("banana")        # length of the string


# In[4]:


len("anil kumar")


# In[5]:


"a"in "banana"       # membership of string


# In[6]:


"y" in "banana"


# In[22]:


st="hello,world"     # slice ranging
st[-2:2]


# In[25]:


st2="madhu"          # printing the string in the reverse order
st2[::-1]


# In[9]:


str1="python "        # concatation of string(addition in case integer)
str2="welcome to "
str2+str1


# In[10]:


str1*3               # repetation of strings (multiplication in case integer)


# In[11]:


str1*4


# In[15]:


name="anil"          # formating of string
age="26"
print("my name is %s,and my age is %s"%(name,age))


# In[16]:


str1.capitalize()    # capitalize the first letter of string


# In[17]:


str1.upper()         # capitalize the whole string


# In[18]:


str1.lower()         # lower casing of string


# In[19]:


st=str1.center(41,"*")    # keep the string in center(41-total length including string)


# In[20]:


len(st)


# In[21]:


st


# In[13]:


str2="banana"


# In[5]:


str2.count("a")          # count the letter(a) repeted in the string(banana)


# In[6]:


str2.find("n")           # gives the index of the letter(n) in string(banana)


# In[7]:


str2.index("n")


# In[37]:


str3= "  avinash,welcome, to  bangalore  "    # removes the spaces in string(not middle) 
str3.strip()


# In[38]:


str4="a v i n a s h"
str4.strip()


# In[39]:


str3.replace('a','zz')         # replacing the string by other string


# In[40]:


str3.title()                  # converting the first letter of all words in a string


# In[1]:


str5= "abcdefghijklmnop"     
str5.split(",")


# In[8]:


"..".join(str5)


# In[ ]:




