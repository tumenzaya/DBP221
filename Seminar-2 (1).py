

# In[49]:


#1
def palindrome(x):
    return x == x[::-1]
x = 'хадгалагдах'
y = palindrome(x) 
if y:
    print("palindrome mun.")
else:
    print("palindrome bish.")


# In[41]:


#2
def tom(str):
    c = 0
    for i in str:
        if i.isupper():
            c += 1
    return c
c = tom('ItIsWhatItIs')
print(c)
def jijig(str):
    s = 0
    for i in str:
        if i.islower():
            s += 1
    return s
s = jijig('ItIsWhatItIs')
print(s)   


# In[14]:


#3 
def urjver(jagsaalt) :
    c = 1
    for i in jagsaalt:
         c = c * i
    return c
urjver([2,4,6,8,10])


# In[30]:


#4
too = 5
f = 1
for i in range(1,too + 1):
    f = f*i
print(f)     


# In[18]:


#5
listt=[1,2,3,4,5]
for i in reversed(listt):
    print(i)


# In[27]:


#6
listt = [1,3,5,7,9]
t = 0
for i in range(len(listt)):
    t = t + listt[i]
print(t)


# In[24]:


#7
a_list = [1,2,3,4,5,1,3,5]
x = set(a_list)
print(x)


# In[25]:


#8
a = 2
b = 1
c = 7
if (a >= b) and (a >= c):
   hamgiin_ih = a
elif (b >= a) and (b >= c):
   hamgiin_ih = b
else:
   hamgiin_ih = c
print("Hamgiin ih too =", hamgiin_ih)


# In[ ]:




