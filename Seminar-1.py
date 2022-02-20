#!/usr/bin/env python
# coding: utf-8

# In[58]:


#1
a_list = ['python','php','java']
print(a_list[0])
print(a_list[1])
print(a_list[2])


# In[18]:


#2
n = [1,3,5,7,9,11,13,15,7,19]
sum = 0
for i in n:
    sum=sum+i
print(sum)


# In[21]:


#3
b = [1,3,5,7,9]
m = 1
for i in b:
    m=m*i
print(m)


# In[27]:


#4
r = [45,56,67,78]
def tt(x,y):
    a=x*y
    return(a)
tt(r[3],r[-1])


# In[28]:


#5
c = [6,8,5,0,3,4,1,2,7,9]
def kk(x,y):
    a=x
    b=y
    return(a,b)
kk(max(c),min(c))


# In[29]:


#6
def gg(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
print(gg(['huslen', 'anaraa', 'nomin', '1221','234']))


# In[6]:


#7 
aa=[8,7,6,7,8,8,7,6,7,8,9]
bb=set(aa)
print(bb)


# In[65]:


#8
k = [1,2,3,4,5]
j = 0
if len(k) > j:
    print('ene jagsaalt hooson bish baina.')
else:
    print('ene jagsaalt hooson baina.')


# In[19]:


#9
too = [1,2,3,4,5,6,7,8,9,0]
ustgah = [4,6]
sort = sorted(ustgah, reverse=True)
for index in ustgah:
    del too[index]
print(too)


# In[57]:


#10
o = (13,25,6,75,35,76)
print(o)


# In[47]:


#11
x = ('german', 'japan', 'america', 'switzerland') 
y = list(x) 
y.append('mongolia') 
x = tuple(y) 
print (x)


# In[10]:


#12
instruments = ('guitar','piano','drums','fleet','calimba')
x = list(instruments)
print(x[2])
print(x[-2])


# In[11]:


#13
sky = ('sun', 'moon', 'stars')
x = ('rainbow')
if x in sky:
    print('baina')
else:
    print('baihgui')


# In[12]:


#14
music = ('rock','r&b','jazz','classical','indie')
for i in music:
    print(i)


# In[31]:


#15
set1 = {'i', 'you', 'she'} 
set2 = {'he', 'we', 'they'} 
sett = set1.union(set2)
print(sett)


# In[32]:


#16
set1 = {'i', 'you', 'she'} 
set2 = {'she', 'i', 'they'} 
seto = set1.intersection(set2)
print(seto)


# In[39]:


#17
nya = {'ichi', 'ni', 'san'} 
print(len(nya))


# In[35]:


#18
set1 = {'i', 'you', 'she'} 
set1.remove('i')
print(set1)


# In[36]:


#19
set1 = {'i', 'you', 'she'} 
set1.clear()
print(set1)


# In[37]:


#20
set1 = {'i', 'you', 'she'} 
del set1
print(set1)


# In[50]:


#21
hp = {'10': 3,
      '21': 1,
      '7': 4,
      '15': 2}
hp1 = sorted([(value, key)
 for (key, value) in hp.items()])
print(hp1)


# In[54]:


#22
harry_potter = {'Author': 'J.K.Rowling',
               'Book1': 'Sorcerers stone',
               'Year': 1997}
if 'Book2' in harry_potter:
    print('baina')
else:
    print('baihgui')


# In[55]:


#23
harry_potter = {'Author': 'J.K.Rowling',
               'Book1': 'Sorcerers stone',
               'Year': 1997}
if 'J.K.Rowling' in harry_potter.values():
    print('baina')
else:
    print('baihgui')


# In[57]:


#24
harry_potter = {'Author': 'J.K.Rowling',
               'Book1': 'Sorcerers stone',
               'Year': 1997}
for x,y in harry_potter.items():
    print(x,y)


# In[59]:


#25
favs = {'Author': 'J.K.Rowling',
               'Book1': 'Sorcerers stone',
               'Year': 1997}
demon_slayer = {'Director': 'Haruo Sotozaki',
               'Season1': 'Kimetsu no yaiba',
               'Release': 2019}
favs.update(demon_slayer)
print(favs)


# In[10]:


#26
dict_1 = {'a': 23,
         'b': 11, 
         'c': 6}
dict_2 = {'c': 10, 
         'b': 12,
         'd': 4}
for key in dict_2:
   if key in dict_1:
      dict_2[key] = dict_1[key] + dict_1[key]
   else:
      pass
dd = dict_1 | dict_2
print(dd)


# In[ ]:




