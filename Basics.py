#BASIC NOTES OF PYTHON
'''Python is a very popular general purpose,interpreted,interacctive object oriented & high level programming launguage.
Developed by "Guido van Rosum" during 1985-1990.'''


#how to check the data types
a=100
b=10.2566
c='classes'
print(type(a))
print(type(b))
print(type(c))


#ASSIGNING OF MULTIPLE INPUTS IN SINGLE LINE

a,b,c =10,3,'abc'
print(a)
print(b)
print(c)


#BSIC OPERATORS

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


#MATHEMATICAL OPERATIONS IN PYTHON

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

    
#LIST DATA TYPE BASICS

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

    
#UPDATING LIST

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


#OBJECT ORIENTED PROGRAM CONCEPT

class Employee:
    name="Ben"
    desig="sales_executive"
    def target(self):
        self.name=123456789
        self.design=10
emp=Employee()
print("emp: ",emp.name,emp.desig)


#MULTIPLICATION TABLE OF A NUMBBERS

a=int(input("enter  the first input  "))
for i in range(1,11):
    table=a*i
    print(a,"x",i,"=",table)
    
    
#EVEN-ODD OF A NUMBBERS
   
a=int(input("enter  the first input  "))  
if a%2==0:
    print('even number')
else:
    print('odd number')
