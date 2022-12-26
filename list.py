#LIST DATA TYPE NOTES

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
    
    
#Index accessing of list
x=[4,5,6,7,8]
y=[8,9,10,11]
print(x[2])
print(y[3])
x[0]=24
print(x)


list1=[]                #empty list
list1.append('sairam')
list1.append(123)
print(list1)


list2=[1,2,3,4]
list3=[5,6,7,8,5,5,5,5,5,5]
list2.extend(list1)
print(list2)
print(list3.count(5))
print(list2.index('sairam'))

#accessing values in list
l4=list3[2:9]
l4

l5=list3[2:6]
l5


z=[1,2,3,4,8,9,12,34,56,75,1334,7617]
print(z[11])
print(len(z))       #length of the list


print(tuple(z))     #type casting (conversion from list to tuple)
p=x+y               #adding of lists
print(p)


print(max(z))       #maximum number in list
print(min(z))       #minimum number in list


for q in [7,8,9]:   #iteration
    print(q)


#pop (REmoves the last number)
list6=[1,2,3,4,5,6,7,8]
list6.pop()


#Insert and order
list7=[1,2,3,4,5,6,7,8]
list7.insert(5,'Sairam')
list7
list7.remove(7)
list7


#Reverse order
list8=[1,2,30,4,565,6,7,8]
list8.reverse()
list8


#Ascending order
list8=[1,2,30,4,565,6,7,8]
list8.sort()
list8


#Descending order
list8=[1,2,30,4,565,6,7,8]
list8.sort(reverse=True)
list8
