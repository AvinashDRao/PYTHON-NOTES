#!/usr/bin/env python
# coding: utf-8

# In[16]:


class Employee:
    def get_details(self):
        self.name="avinash"
        self.age=28
        print("name: ", self.name)
        print("age: ", self.age)
    def print_info(self):
        print("employee name is: ",self.name)
        print("employee age is: ",self.age)
        
emp1=Employee()
emp2=Employee()
emp1.get_details()


# In[20]:


emp1.print_info()


# In[98]:


class Employee:
    name="Ben"
    age=36
    desig="sales eecutive"
    def target(self,sales):
        self.sales=20
        if self.sales>5:
            print("achived")
        else:
            print("failsed to achieve")
employee1=Employee()
employee2=Employee()
    


# In[99]:


employee1.name


# In[100]:


employee2.target(25)


# In[101]:


employee2.name="sairam"
employee2.age=42
print("employee1 name is: ",employee1.name)
print("employee1 age is: ",employee1.age)
print("employee2 name is: ",employee2.name)
print("employee2 age is: ",employee2.age)


# In[ ]:


'''1.What is Encapsulation ?
        Hiding the implementtion details from the end user is called encapsulation.
   2.What is abstraction ?
        Abstraction is the process of steps followed to achieve encapsulation'''

# Class Library = Display available books, lend a book, Add a book
# Class Customer = Request book, Return book

class Library:
        
        def __init__(self,list_books):
            self.avilable_books=list_books
            
        def display_available_books(self):
            print() 
            print("Available books in the library are ")
            for book in self.avilable_books:
                print(book)
            
        def lend_books(self,requested_book):
            if requested_book in self.available_book:
                self.available_books.remove(requeted_book)
                print("Thank you for lending the book")
            else:
                print("Sorry the requested book is not available")
            
        def add_books(self,return_book):
            self.available_books.append(return_book)
            print("Thank you for returning the book !!!")
            
        
class Customer:
    
        def request_books(self):
            self.requested_book=input("Please enter the book you want: ")
            return self.requested_book

        def return_books(self):
            print("Enter the name of the book you wanted to return: ")
            return_book=input()
            return return_book
      
library = Library(["think a like a monk","think and grow rich","2 states"])
customer = Customer

while True:
    print("Enter 1 to display the available books ")
    print("Enter 2 to request for a books ")
    print("Enter 3 for returning the books ")
    print("Enter 4 to exit ")
    user_choice = int(input("Enter your choice: "))
    if user_chioce == 1:
        library.display_available_books()
    elif user_chioce == 2:
        requested_book=customer.request_book()
        library.lend_books(requested_book)
    elif user_chioce == 3:
        return_book=customer.retun_book()
        library.add_books(return_book)
    elif user_chioce == 4:
        quit()
    else:
        print("please enter appropriate value ")


# In[ ]:



    
    


# In[ ]:





# 

# In[ ]:




