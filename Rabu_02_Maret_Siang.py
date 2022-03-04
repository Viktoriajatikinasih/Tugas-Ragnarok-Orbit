#!/usr/bin/env python
# coding: utf-8

# In[19]:


print("Nomor 1")


# In[3]:


def divisible (m,n):
    if (m % n == 0):
        return True

    else :
        return False

print(divisible(22,5))
print(divisible(80,20))


# In[20]:


print("Nomor 2")


# In[42]:


def main_menu():
    print("Welcome To Victory Cafe")
    print('='*20)
    print('='*10, "MAIN MENU",'='*10)
    print(" 1. |Soup and salad       | ")
    print(" 2. |Pasta with meat sauce| ")
    print(" 3. |Chef’s special       | ")
    print('='*20)
    
    number = input("Which number would you like to order? ")
    if number == '1':
        print('One Soup and salad coming right up!')
    elif number == '2':
        print('One Pasta with meat sauce coming right up!')
    elif number == '3':
        print('One Chef’s special coming right up!')
    else :
        print('Sorry, that is not a valid choice.')
# main program
if __name__=='__main__':
    main_menu()


# In[2]:


print("Nomor 3")


# In[10]:


def rand_divis_3 ():
    x=int(input("Masukkan bilangan: "))
    
    if (x % 3 == 0):
        return True

    else :
        return False
print(rand_divis_3())


# In[11]:


print("Nomor 4")


# In[22]:


1 != 1


# In[24]:


def not_equal(x,y):
    if (x != y):
        return True
    else :
        return False
print(not_equal(3,2))


# In[26]:


def not_equal(x,y):
    if (not (x == y)):
        return True
    else :
        return False
print(not_equal(3,2))


# In[38]:


print("Nomor 5")


# In[36]:


def ask_name():
    name = input("Enter your name: ")

ask_name()
print("Your name is", name)


# In[87]:


name = input("Enter your name: ")
print("Your name is", name)


# In[73]:


print ('atau')


# In[89]:


def ask_name(name):
    print("Your name is", name)
ask_name("Vikto")


# In[ ]:





# In[ ]:




