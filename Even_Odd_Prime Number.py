#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# WAP OF EVEN_ODD_PRIME NUMBER
user_input=int(input('Enter the number:  '))
if user_input==0:
    print ('user_input is invalid number')
else:
    if user_input>1:
        for i in range(2,user_input):
            if   (user_input%i)==0:
                print ('user_input is not a prime number')
                break
        else:
            print ('user_input is a prime number') 
    else:
        print ('user_input is a prime number')

    if (user_input % 2)==0:
        print('User_input is even number')
    else:
        print('User_input is odd number')

