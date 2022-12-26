#!/usr/bin/env python
# coding: utf-8

# In[4]:


a,b,c=1,"ok",2
a


# In[2]:


b


# In[5]:


c


# In[6]:


b


# In[11]:


a,b,c=1,2,3
print(a,b,c)
type(b)


# In[ ]:


a=int(input('enter the number  '))
if a in range(0,10):
    print(a*100)
if a in range (10,100):
    print(a**5)
if a in range(100,1000):
    b=int(input('enter the input  '))
    print(a+b)


# In[ ]:


a=int(input('enter the number  '))
if a in range(0,10):
    print(a*100)
if a in range (10,100):
    print(a**5)
if a in range(100,1000):
    b=int(input('enter the input  '))
    print(a+b)


# In[ ]:


#how to check the data types
a=100
b=10.2566
c='classes'
print(type(a))
print(type(b))
print(type(c))
#muliple assignments
a,b,c =10,3,'abc'
print(a)
print(b)
print(c)

#functins of operators
print('the sum is: ', a+b)
d=a/b
print(d)
e=a**b     #exponential
print(e)
f=a%b      #modulus
print(f)
g=a//b     #floor division
print(g)

#comparision operators
if a==b:
    print("equal")
if a!=b:
    print("not equal")


# In[ ]:


def add(a,b):
    sum=a*b
    print(sum)
def sub(a,b):
    dif=a-b
    print(dif)
def mul(a,b):
    multi=a*b
    print(multi)
def div(a,b):
    div=a/b
    print(div)

if __name__=="__main__":
    ssum=add(10,20)


# In[ ]:


x=[4,5,6,7,8]
y=[8,9,10,11]
if 8 in x:
    print('true')
else:
    print("false")
if 6 not in x:
    print('true')
else:
    print("false")

#updating list
print(x[2])
print(y[3])
x[0]=24
print(x)
z=[1,2,3,4,8,9,12,34,56,75,1334,767]
print(z[11])
print(len(z))       #length of the list
print(max(z))       #maximum number in list
print(min(z))       #minimum number in list
print(tuple(z))     #type casting (conversion from list to tuple)
p=x+y               #adding of lists
print(p)
for q in [7,8,9]:   #iteration
    print(q)

list1=[]                #empty list
list2=[1,2,3,4]
list3=[5,6,7,8,5,5,5,5,5,5]
list1.append('sairam')
list1.append(123)
print(list1)

list2.extend(list1)
print(list2)
print(list3.count(5))
print(list2.index('sairam'))
#accessing values in list
l4=list3[2:9]
print(l4)
l5=list3[2:6]
print(l5)


# In[ ]:


class Employee:
    name="Ben"
    desig="sales_executive"
    def target(self):
        self.name=123456789
        self.design=10
emp=Employee()
print("emp: ",emp.name,emp.desig)


# In[ ]:


a=int(input("enter  the first input  "))
for i in range(1,11):
    table=a*i
    print(a,"x",i,"=",table)
if a%2==0:
    print('even number')
else:
    print('odd number')


# In[ ]:




