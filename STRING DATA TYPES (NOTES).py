# Data types:

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


for letter in "banana":
    print(letter)


len("banana")        # length of the string


len("anil kumar")


"a"in "banana"       # membership of string


"y" in "banana"


st="hello,world"     # slice ranging
st[-2:2]


st2="madhu"          # printing the string in the reverse order
st2[::-1]


str1="python "        # concatation of string(addition in case integer)
str2="welcome to "
str2+str1

str1*3               # repetation of strings (multiplication in case integer)


str1*4


name="anil"          # formating of string
age="26"
print("my name is %s,and my age is %s"%(name,age))


str1.capitalize()    # capitalize the first letter of string


str1.upper()         # capitalize the whole string


str1.lower()         # lower casing of string


st=str1.center(41,"*")    # keep the string in center(41-total length including string)


len(st)

st

str2="banana"

str2.count("a")          # count the letter(a) repeted in the string(banana)

str2.find("n")           # gives the index of the letter(n) in string(banana)


str2.index("n")


str3= "  avinash,welcome, to  bangalore  "    # removes the spaces in string(not middle) 
str3.strip()


str4="a v i n a s h"
str4.strip()


str3.replace('a','zz')         # replacing the string by other string

str3.title()                  # converting the first letter of all words in a string

str5= "abcdefghijklmnop"     
str5.split(",")


# In[8]:


"..".join(str5)
